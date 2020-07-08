from django.urls import path
from rest_framework.routers import DefaultRouter
from mainapp.views import (
	PostOfficeViewSet,
	NewspaperViewSet,
	PrintingHouseViewSet,
	OrderViewSet,
	OrderViewSet_raw,
	PrintRunViewSet,
	CreatePrintRunsViewSet,
	UpdatePrintRuns,
	PHAddress,
	EditorName,
	PostOfficeAddress,
	NewspaperNameAndPostOfficeNum,
	PostOfficeInfo,
	)


router = DefaultRouter()
router.register("po_list", PostOfficeViewSet)
router.register("np_list", NewspaperViewSet)
router.register("ph_list", PrintingHouseViewSet)
router.register("o_list", OrderViewSet)
router.register("o_list2", OrderViewSet_raw)
router.register("pr_create", CreatePrintRunsViewSet)
router.register("pr_update", UpdatePrintRuns)
router.register("pr_list", PrintRunViewSet)
router.register("func1", PHAddress)
router.register("func2", EditorName)
router.register("func3", PostOfficeAddress)
router.register("func4", NewspaperNameAndPostOfficeNum)
router.register("func5", PostOfficeInfo)

urlpatterns = router.urls


