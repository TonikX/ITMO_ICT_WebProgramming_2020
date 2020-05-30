from django.db import models


class Subject(models.Model):
	TYPES = (
		('major', 'major'),
		('minor', 'minor')
	)
	name = models.CharField(max_length=20, primary_key=True)
	sub_type = models.CharField(max_length=5, choices=TYPES)

	def __str__(self):
		return self.name


class Teacher(models.Model):
	GENDERS = (
		('male', 'male'),
		('female', 'female'),
		('non-binary', 'non-binary')
	)
	name = models.CharField(max_length=50, primary_key=True)
	gender = models.CharField(max_length=10, choices=GENDERS)
	experience = models.CharField(max_length=50)
	subjects = models.ManyToManyField(Subject, through='Teaching')

	def __str__(self):
		return self.name


class Teaching(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	def __str__(self):
		return self.teacher.name + ': ' + self.subject.name


class Room(models.Model):
	number = models.CharField(max_length=4, primary_key=True)
	floor = models.IntegerField()
	subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
	teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.number  #+ ' ' + self.subject.name  #+ ' ' + self.teacher.name  # убрать все кроме нумера


class Class(models.Model):
	name = models.CharField(max_length=3, primary_key=True)
	guiding_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name


class Pupil(models.Model):
	GENDERS = (
		('male', 'male'),
		('female', 'female'),
		('non-binary', 'non-binary')
	)
	name = models.CharField(max_length=50, primary_key=True)
	gender = models.CharField(max_length=10, choices=GENDERS)
	study_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name  #+ ' ' + self.study_class.name


class Assessment(models.Model):
	GRADES = (
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5')
	)
	term = models.IntegerField(default=4)
	pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	grade = models.IntegerField(choices=GRADES, default=4)

	def __str__(self):
		return self.pupil.name + ': ' + self.subject.name


class Timetable(models.Model):
	DAYS = (
		('Mon', 'Monday'),
		('Tue', 'Tuesday'),
		('Wed', 'Wednesday'),
		('Thu', 'Thursday'),
		('Fri', 'Friday')
	)
	NUMBERS = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
	)
	day_of_week = models.CharField(max_length=3, choices=DAYS)
	study_class = models.ForeignKey(Class, on_delete=models.CASCADE)
	lesson_num = models.IntegerField(choices=NUMBERS)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

	def __str__(self):
		return self.study_class.name + ' | ' + self.day_of_week
