from django_filters import rest_framework as filters

from .models import PrintRun

class PrintRunFilter(filters.FilterSet):
	class Meta:
		model = PrintRun
		fields = "__all__"


class PrintRunFunc3Filter(filters.FilterSet):
	prNpCode__npPrice = filters.RangeFilter()
	class Meta:
		model = PrintRun
		fields = ('prNpCode__npPrice', )


class PrintRunFunc4Filter(filters.FilterSet):
	prPrintRun = filters.RangeFilter()
	class Meta:
		model = PrintRun
		fields = ('prPrintRun', )

