# Copyright (c) 2010, 2014 Antti Heinonen <heinoan@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from socket import socket, AF_UNIX, AF_INET, SOCK_STREAM, SOL_TCP, TCP_NODELAY, MSG_WAITALL
from struct import pack, unpack
from operator import itemgetter, methodcaller

AUTHENTICATIONREQUEST	= b"R"[0]
ERRORRESPONSE			= b"E"[0]
PARAMETERDESCRIPTION	= b"t"[0]
ROWDESCRIPTION			= b"T"[0]
DATAROW					= b"D"[0]
NODATA					= b"n"[0]
COMMANDCOMPLETE			= b"C"[0]
PARSECOMPLETE			= b"1"[0]
BINDCOMPLETE			= b"2"[0]
CLOSECOMPLETE			= b"3"[0]
PARAMETERSTATUS			= b"S"[0]
BACKENDKEYDATA			= b"K"[0]
READYFORQUERY			= b"Z"[0]

SYNC		= b"S\x00\x00\x00\x04"
FLUSH		= b"H\x00\x00\x00\x04"
EXECUTE		= b"E\x00\x00\x00\t\x00\x00\x00\x00\x00"
TERMINATE	= b"X\x00\x00\x00\x04"

text = methodcaller("decode")

types = {
	16: lambda x: x == b't',
	20: int,
	21: int,
	23: int,
}

errors = {
	67: "Code",
	68: "Detail",
	70: "File",
	72: "Hint",
	76: "Line",
	77: "Message",
	80: "Position",
	82: "Routine",
	83: "Severity",
	87: "Where",
	112: "Internal position",
	113: "Internal query",
}

def AuthenticationRequest(data):
	return unpack("!i", data[:4])[0], data[4:]

def ErrorResponse(data):
	lines = []
	for field in data[:-2].split(b"\x00"):
		lines.append(errors[field[0]] + ": " + field[1:].decode())
	raise Error("\n\t" + "\n\t".join(lines))

def ParameterDescription(data):
	pass

def RowDescription(data):
	count = unpack("!h", data[:2])[0]
	data = data[2:]
	field_names = []
	field_types = []
	for field in range(count):
		name, data = data.split(b"\x00", 1)
		desc = unpack("!ihihih", data[:18])
		data = data[18:]
		field_names.append("" if name[0] == b"?" else name.decode())
		field_types.append(types.get(desc[2], text))
	return field_names, field_types

class DataRow:
	def __init__(self, data):
		self.data = data

	def __call__(self, types):
		count = unpack("!h", self.data[:2])[0]
		row = []
		o = 2
		for i in range(count):
			size = unpack("!i", self.data[o:o + 4])[0]
			o += 4
			if size == -1:
				row.append(None)
			else:
				row.append(types[i](self.data[o:o + size]))
				o += size
		return row

class Type(type):
	def __new__(cls, name, base, attr):
		for i, name in enumerate(attr.pop("__cols__", ())):
			if name:
				attr[name] = property(itemgetter(i))
		attr["__slots__"] = ()
		return type.__new__(cls, name, base, attr)

class Row(tuple, metaclass = Type):
	pass

class Error(Exception):
	pass

class PreparedStatement:
	def __init__(self, send_message, read_message, statement, factory = tuple):
		self.send_message = send_message
		self.read_message = read_message
		self.statement = statement
		self.send_message(self.__parse() + self.__describe() + SYNC + FLUSH)
		while self.read_message() != PARSECOMPLETE: pass
		param_desc = self.read_message()
		field_desc = self.read_message()
		if field_desc != NODATA:
			self.factory = Type("Row", (factory,), { "__cols__": field_desc[0] })
			if hasattr(self.factory, "_new"):
				self.factory = self.factory._new
			self.types = field_desc[1]

	def __repr__(self):
		return self.statement

	def __enter__(self):
		return self

	def __exit__(self, error, value, traceback):
		self.close()
		if error:
			raise

	def __call__(self, *args):
		self.send_message(self.__bind(*args) + EXECUTE + SYNC + FLUSH)
		while self.read_message() != BINDCOMPLETE: pass
		return self

	def __iter__(self):
		return self

	def __next__(self):
		row = self.read_message()
		if row == COMMANDCOMPLETE:
			raise StopIteration
		return self.factory(row(self.types))

	def all(self, *args):
		self(*args)
		result = []
		row = self.read_message()
		while row != COMMANDCOMPLETE:
			result.append(self.factory(row(self.types)))
			row = self.read_message()
		return result

	def first(self, *args):
		self(*args)
		row = self.read_message()
		if row == COMMANDCOMPLETE:
			return None
		if len(self.types) == 1:
			return row(self.types)[0]
		return self.factory(row(self.types))

	def close(self):
		self.send_message(self.__close() + FLUSH)
		while self.read_message() != CLOSECOMPLETE: pass

	def __parse(self):
		self.name = "ps_{}".format(hash(self.statement)).encode() + b"\x00"
		msg = self.name + self.statement.encode() + b"\x00\x00\x00"
		return b"P" + pack("!i", len(msg) + 4) + msg

	def __describe(self):
		return b"D" + pack("!i", len(self.name) + 5) + b"S" + self.name

	def __bind(self, *args):
		msg = b"\x00" + self.name + b"\x00\x00" + pack("!h", len(args))
		for arg in args:
			if arg is None:
				msg += b"\xff\xff\xff\xff"
			else:
				arg = str(arg).encode()
				msg += pack("!i", len(arg)) + arg
		msg +=  b"\x00\x00"
		return b"B" + pack("!i", len(msg) + 4) + msg

	def __close(self):
		return b"C" + pack("!i", len(self.name) + 5) + b"S" + self.name

class Transaction:
	def __init__(self, connection):
		self.begin = connection.begin
		self.commit = connection.commit
		self.rollback = connection.rollback

	def __enter__(self):
		self.begin()

	def __exit__(self, error, value, traceback):
		if error:
			self.rollback()
			raise
		self.commit()

class Connection:
	def __init__(self, address = ("localhost", 5432), user = "postgres", password = None, database = None):
		if isinstance(address, str):
			self.sock = socket(AF_UNIX, SOCK_STREAM)
			self.sock.connect(address)
		else:
			self.sock = socket(AF_INET, SOCK_STREAM)
			self.sock.setsockopt(SOL_TCP, TCP_NODELAY, 1)
			self.sock.connect(address)
		self.__send_message(self.__startup(user, database))
		code, salt = self.__read_message()
		if code in (3, 5):
			if not password:
				raise Error("server requested a password but none was provided")
			self.__send_message(self.__password(user, password, salt))
		elif code != 0:
			raise Error("authentication method {} not supported".format(code))
		while self.__read_message() != READYFORQUERY: pass
		self.begin = PreparedStatement(self.__send_message, self.__read_message, "BEGIN")
		self.commit = PreparedStatement(self.__send_message, self.__read_message, "COMMIT")
		self.rollback = PreparedStatement(self.__send_message, self.__read_message, "ROLLBACK")

	def __call__(self, *args):
		p = self.prepare(args[0])
		r = p.all(*args[1:])
		p.close()
		return r

	def __enter__(self):
		return self

	def __exit__(self, error, value, traceback):
		self.close()
		if error:
			raise

	def transaction(self):
		return Transaction(self)

	def prepare(self, *args, **kargs):
		return PreparedStatement(self.__send_message, self.__read_message, *args, **kargs)

	def close(self):
		self.__send_message(TERMINATE)
		self.sock.close()

	def __send_message(self, data):
		self.sock.sendall(data)

	def __read_message(self):
		code, size = unpack("!bi", self.sock.recv(5, MSG_WAITALL))
		if size > 4:
			data = self.sock.recv(size - 4, MSG_WAITALL)
		if code == DATAROW:
			return DataRow(data)
		elif code == ERRORRESPONSE:
			return ErrorResponse(data)
		elif code == PARAMETERDESCRIPTION:
			return ParameterDescription(data)
		elif code == ROWDESCRIPTION:
			return RowDescription(data)
		elif code == AUTHENTICATIONREQUEST:
			return AuthenticationRequest(data)
		return code

	@staticmethod
	def __startup(user, database):
		msg = b"\x00\x03\x00\x00user\x00" + user.encode() + b"\x00"
		if database:
			msg += b"database\x00" + database.encode() + b"\x00"
		msg += b"client_encoding\x00UTF8\x00\x00"
		return pack("!i", len(msg) + 4) + msg

	@staticmethod
	def __password(user, password, salt):
		if salt:
			from hashlib import md5
			msg = md5(password.encode() + user.encode()).hexdigest().encode()
			msg = b"md5" + md5(msg + salt).hexdigest().encode() + b"\x00"
		else:
			msg = password.encode() + b"\x00"
		return b"p" + pack("!i", len(msg) + 4) + msg