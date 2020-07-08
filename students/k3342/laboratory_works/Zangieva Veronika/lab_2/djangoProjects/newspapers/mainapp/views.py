from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import PrintingHouse, PostOffice, Newspaper, Order, PrintRun
from .filters import PrintRunFilter, PrintRunFunc3Filter, PrintRunFunc4Filter
from mainapp.serializers import (
	PostOfficeSerializer,
	NewspaperSerializer,
	PrintingHouseSerializer,
	OrderSerializer,
	OrderSerializer_raw,
	PrintRunSerializer,
	PrintRunFunc1Ser,
	PrintRunFunc2Ser,
	PrintRunFunc3Ser,
	PrintRunFunc4Ser,
	PrintRunFunc5Ser
	)


class PostOfficeViewSet(ModelViewSet):
	serializer_class = PostOfficeSerializer
	queryset = PostOffice.objects.all()


class NewspaperViewSet(ModelViewSet):
	serializer_class = NewspaperSerializer
	queryset = Newspaper.objects.all()


class PrintingHouseViewSet(ModelViewSet):
	serializer_class = PrintingHouseSerializer
	queryset = PrintingHouse.objects.all()


class OrderViewSet(ModelViewSet):
	serializer_class = OrderSerializer
	queryset = Order.objects.all()


class OrderViewSet_raw(ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer_raw


class PrintRunViewSet(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunSerializer	
	filter_backends = (DjangoFilterBackend,)
	filterset_class = PrintRunFilter


def splitCount(orderNpCount, openedPhCount):
	splited = []
	div = orderNpCount//openedPhCount
	for i in range(openedPhCount):
		splited.append(div)
	splited[-1] = splited[-1] + (orderNpCount%openedPhCount)

	return splited


class CreatePrintRunsViewSet(ModelViewSet):
	"""Формирование тиражей по последнему заказу"""	
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = PrintRunFilter

	def get_queryset(self):
		lastOrder = Order.objects.last()
		postOffice = lastOrder.oPoCode
		newspaper = lastOrder.oNpCode
		orderNpCount = lastOrder.oNpCount
		openedPH = PrintingHouse.objects.filter(phWorkStatus='открыта')
		printRuns = splitCount(orderNpCount, len(openedPH))

		i = 0
		for printingHouse in openedPH:			
			PrintRun.objects.create(
				prOCode=lastOrder,
				prPoCode=postOffice,
				prNpCode=newspaper,
				prPhCode=printingHouse,
				prPrintRun=printRuns[i]
			)
			i += 1


class UpdatePrintRuns(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = PrintRunFilter
	

	def get_queryset(self):
		closedPHList = PrintingHouse.objects.filter(phWorkStatus='закрыта').values_list('id', flat=True)
		for PH in closedPHList:
			# по коду закрытой типографии получаем список id заказов, тиражи которых необходимо обнулить
			orderList = list(set(PrintRun.objects.filter(prPhCode=PH).values_list('prOCode', flat=True)))
			for orderId in orderList:
				printRunsNeededUpdate = PrintRun.objects.filter(prOCode=orderId, prPhCode=PH)
				printRunsNeededUpdate.update(prPrintRun=0)

		openedPHObjects = PrintingHouse.objects.filter(phWorkStatus='открыта')
		for PH in openedPHObjects:
			printingHouseId = PH.id
			# по коду открытой типографии получаем список id заказов, тиражи которых необходимо перерасчитать
			orderList = list(set(PrintRun.objects.filter(prPhCode=printingHouseId).values_list('prOCode', flat=True)))		
			for orderId in orderList:
				# по id заказа находим тиражи, которые надо обновить
				printRunsNeededUpdate = PrintRun.objects.filter(prOCode=orderId)			
				# берем объект тиража для обновления
				for printRunObject in printRunsNeededUpdate:
					order = printRunObject.prOCode
					postOffice = order.oPoCode
					newspaper = order.oNpCode
					printingHouse = printRunObject.prPhCode
					orderNpCount = order.oNpCount
					printRuns = splitCount(orderNpCount, len(openedPHObjects))

					i = 0
					for printingHouse in openedPHObjects:
						printRunsNeededUpdate.filter(prPhCode=printingHouse, prOCode=order).update_or_create(
							defaults={
							'prPrintRun': printRuns[i]
							},
							prOCode=order,
							prPoCode=postOffice,
							prPhCode=printingHouse,
							prNpCode=newspaper,
						)
						i += 1


class PHAddress(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunFunc1Ser
	filter_backends = (DjangoFilterBackend,)
	filter_fields=("prNpCode__npName",)

	def get_queryset(self):
		queryset = PrintRun.objects.values('prPhCode__phAddress').exclude(prPrintRun=0).distinct()
		return queryset


class EditorName(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunFunc2Ser
	filter_backends = (DjangoFilterBackend,)

	def get_queryset(self):
		maxPrintRun = PrintRun.objects.values('prPrintRun').order_by('-prPrintRun').first()['prPrintRun']
		queryset = PrintRun.objects.filter(prPrintRun=maxPrintRun).values('prNpCode__npEditorName', 'prPrintRun')		
		return queryset


class PostOfficeAddress(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunFunc3Ser
	filterset_class = PrintRunFunc3Filter
	filter_backends = (DjangoFilterBackend,)

	def get_queryset(self):
		queryset = PrintRun.objects.distinct().values('prPoCode__poAddress').exclude(prPrintRun=0)
		return queryset


class NewspaperNameAndPostOfficeNum(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunFunc4Ser
	filterset_class = PrintRunFunc4Filter
	filter_backends = (DjangoFilterBackend,)

	def get_queryset(self):
		queryset = PrintRun.objects.values('prNpCode__npName',
												'prPoCode__poNum',
												'prPrintRun').exclude(
																prPrintRun=0).distinct().order_by('-prPrintRun')
		return queryset


class PostOfficeInfo(ModelViewSet):
	queryset = PrintRun.objects.all()
	serializer_class = PrintRunFunc5Ser
	filter_backends = (DjangoFilterBackend,)
	filter_fields=("prNpCode__npName", "prPhCode__phAddress")

	def get_queryset(self):
		queryset = PrintRun.objects.values('prPoCode__poNum', 'prPoCode__poAddress', 'prPrintRun').exclude(prPrintRun=0)
		return queryset


