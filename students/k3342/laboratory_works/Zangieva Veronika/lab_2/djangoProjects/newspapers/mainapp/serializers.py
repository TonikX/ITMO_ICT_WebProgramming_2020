from rest_framework import serializers

from .models import PrintingHouse, PostOffice, Newspaper, Order, PrintRun


class PostOfficeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostOffice
		fields = "__all__"


class NewspaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Newspaper
		fields = "__all__"


class PrintingHouseSerializer(serializers.ModelSerializer):
	class Meta:
		model = PrintingHouse
		fields = "__all__"


class getPostOfficeNumSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostOffice
		fields = ('poNum',)		


class getNewspaperNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Newspaper
		fields = ('npName',)


class OrderSerializer(serializers.ModelSerializer):
	oPoCode = getPostOfficeNumSerializer()
	oNpCode = getNewspaperNameSerializer()
	class Meta:
		model = Order
		fields = "__all__"


class OrderSerializer_raw(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = "__all__"


class PrintRunSerializer(serializers.ModelSerializer):
	class Meta:
		model = PrintRun
		fields = "__all__"


class PrintRunFunc1Ser(serializers.ModelSerializer):
	phAddress = serializers.CharField(source='prPhCode__phAddress')
	class Meta:
		model = PrintRun
		fields = ('phAddress',)


class PrintRunFunc2Ser(serializers.ModelSerializer):	
	npEditorName = serializers.CharField(source='prNpCode__npEditorName')
	class Meta:
		model = PrintRun
		fields = ('npEditorName', 'prPrintRun')


class PrintRunFunc3Ser(serializers.ModelSerializer):	
	poAddress = serializers.CharField(source='prPoCode__poAddress')
	class Meta:
		model = PrintRun
		fields = ('poAddress', )


class PrintRunFunc4Ser(serializers.ModelSerializer):
	npName = serializers.CharField(source='prNpCode__npName')
	poNum = serializers.CharField(source='prPoCode__poNum')
	class Meta:
		model = PrintRun
		fields = ('npName', 'poNum', 'prPrintRun')


class PrintRunFunc5Ser(serializers.ModelSerializer):
	poNum = serializers.CharField(source='prPoCode__poNum')
	poAddress = serializers.CharField(source='prPoCode__poAddress')

	class Meta:
		model = PrintRun
		fields = ('poNum', 'poAddress')
