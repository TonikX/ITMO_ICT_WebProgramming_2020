from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import datetime
from .models import *
from .serializers import *
from django.db.models import Count,Sum,Avg,Min,Max,\
                            F,DurationField,ExpressionWrapper
from itertools import chain
from rest_framework.parsers import JSONParser


class Report_buses(APIView):
    def get(self,request):
        #buses=Bus.objects.order_by('type').exclude(id=4)
        #res1 = Driver.objects.filter(bus__in = buses).order_by('bus__type')

        # num of bus types (not necessarily driven)
        b_types = Bus.objects.exclude(id=4).values('type').annotate(Count("id")).order_by('type')
        # num of bus types (tied to drivers => are used)
        #res = Driver.objects.filter(bus__in = buses).values("bus__type").annotate(Count("bus__type")).order_by('bus__type')

        #
        age_exp = Driver.objects.annotate(age=ExpressionWrapper(
            datetime.date.today() - F('d_of_b'),
            output_field=DurationField()),exp_days=ExpressionWrapper(
            datetime.date.today() - F('date_begin'),
            output_field=DurationField())).values(
                'age','exp_days',
                'surname','name','passport')

        avg_age_exp = Driver.objects.annotate(age=ExpressionWrapper(
            datetime.date.today() - F('d_of_b'),
            output_field=DurationField()),exp_days=ExpressionWrapper(
            datetime.date.today() - F('date_begin'),
            output_field=DurationField())).values(
            'age','exp_days').aggregate(Avg('age'),Avg('exp_days'))


        # routes with buses of type X
        route_for_type1 = Driver.objects.filter(bus__type =1).values('route').distinct()
        route_for_type2 = Driver.objects.filter(bus__type =2).values('route').distinct()
        route_for_type3 = Driver.objects.filter(bus__type =3).values('route').distinct()
        route_for_type4 = Driver.objects.filter(bus__type =4).values('route').distinct()
        route_for_type5 = Driver.objects.filter(bus__type =5).values('route').distinct()

        #r = Driver.objects.all().values('bus__type','route__num').order_by('bus__type')
        #serializer = DriverSerializers(res,many=True)
        return Response({"avg_age_exp":avg_age_exp, "age_exp": age_exp,
                         "r_for_t1":route_for_type1, "r_for_t2":route_for_type2,
                         "r_for_t3":route_for_type3, "r_for_t4":route_for_type4,
                         "r_for_t5":route_for_type5, "bus_types":b_types})
        #return Response({"data": serializer.data})



class DriverOnRoute(APIView):
    def get(self, request):
        route_id = request.GET.get("route")
        # just are here!
        drivers_const = Driver.objects.filter(route=route_id)

        # are here bc someone is sick / bus is broken / etc
        #sch_drivers_temp = Schedule.objects.filter(route=route_id).exclude(driver__in = drivers_const)
        sch_drivers_const = Schedule.objects.filter(driver__in = drivers_const).order_by('driver')
        #all_sch = sch_drivers_const.union(sch_drivers_temp)

        serializerSch = ScheduleSerializers(sch_drivers_const,many=True)
        serializerDr = DriverSerializers(drivers_const, many=True)
        return Response({"drivers":serializerDr.data,"scheds": serializerSch.data})

class BusOnRoute(APIView):
    def get(self,request):
        scheds=Schedule.objects.values("route__num").annotate(Min('work_start'),Max('work_end'))
        return Response({"data": scheds})

class RouteTime(APIView):
    def get(self,request):
        whole_time = Route.objects.aggregate(Sum('circle_time_min'))
        return Response({"data": whole_time})

class BusReport(APIView):
    def get(self, request):
        day = request.GET.get("work_day")
        scheds = Schedule.objects.filter(work_day=day)
        bad_reports = Report.objects.filter(
            schedule_line__in = scheds).exclude(
            reason=0).order_by('schedule_line__bus')
        buses = Report.objects.filter(
            schedule_line__in = scheds).exclude(reason=0).values(
            'schedule_line__bus__reg_plate','schedule_line__bus').distinct()

        serializer = ReportSerializers(bad_reports, many=True)
        # ~ work_day: bus(reason) + sch_line?..
        return Response({"buses":buses,"data": serializer.data})


class DriverClass(APIView):
    def get(self, request):
        #route_id = request.GET.get("route")
        drivers=Driver.objects.order_by('job_class').values("job_class").annotate(Count('job_class'))
        d1 = Driver.objects.filter(job_class=1).values('passport','surname','name')
        d2 = Driver.objects.filter(job_class=2).values('passport','surname','name')
        d3 = Driver.objects.filter(job_class=3).values('passport','surname','name')

        #drivers=Driver.objects.values("job_class").annotate(dcount=Count('job_class'))

        #serializer = DriverSerializers(drivers, many=True)
        return Response({"data": drivers,"dr_1":d1,"dr_2":d2,"dr_3":d3})




class AllDrivers(APIView):
    def get(self, request):
        drivers = Driver.objects.all().order_by('surname')
        serializer = DriverSerializers(drivers,
                                       many=True)
        return Response({"data":serializer.data})


class Drivers(APIView):
    def post(self, request):
        driver = DriverPostSerializers(data=request.data)
        if driver.is_valid():
            # schedule.save(driver = request.driver)
            driver.save()
            return Response({"status": "Add"})
        else:
            return Response(driver.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        #drivers = Driver.objects.all()
        id = request.GET.get("id")
        drivers = Driver.objects.filter(id=id)
        serializer = DriverSerializers(drivers,
                                       many=True)
        return Response({"data":serializer.data})

class Drivers_detail(APIView):
    def delete(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        driver.delete()
        return Response({"status": "Delete"})


class Buses(APIView):
    def get(self, request):
        buses = Bus.objects.exclude(id=4)
        serializer = BusSerializers(buses,
                                       many=True)
        return Response({"data":serializer.data})


class Malfunctions(APIView):
    def get(self, request):
        mals_open = Malfunction.objects.filter(date_close = None).order_by('-date_start')
        mals_closed = Malfunction.objects.exclude(date_close = None).order_by('-date_close')
        #mals = Malfunction.objects.all().order_by('-date_start')
        serializerOpen = MalfunctionSerializers(mals_open,many=True)
        serializerClosed = MalfunctionSerializers(mals_closed, many=True)
        return Response({"open":serializerOpen.data,"closed":serializerClosed.data})

    def post(self, request):
        #sch = Schedule(bus=self.request.bus)
        busmal = MalfunctionPostSerializers(data = request.data)
        if busmal.is_valid():
            busmal.save()
            return Response({"status":"Add"})
        else:
            return Response(busmal.errors, status=status.HTTP_400_BAD_REQUEST)


class Malfunctions_detail(APIView):
    def put(self, request, pk):
        mals = Malfunction.objects.get(pk=pk)
        serializer = MalfunctionSerializers(mals,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Changed"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Routes(APIView):
    def get(self, request):
        #driver = request.get.data('')
        routes = Route.objects.exclude(id=3)
        serializer = RouteSerializers(routes,
                                      many=True)
        return Response({"data":serializer.data})


class Routes_detail(APIView):
    def get(self, request):
        id = request.GET.get("id")
        routes = Route.objects.filter(id=id)
        serializer = RouteSerializers(routes,
                                      many=True)
        return Response({"data":serializer.data})


class BusesStatus(APIView):
    def get(self, request):
        buses = Bus.objects.exclude(id=4)
        mals_open_buses = Malfunction.objects.filter(date_close = None).order_by('-date_start').values('bus_id')
        workingBuses = buses.exclude(id__in = mals_open_buses)
        brokenBuses = buses.filter(id__in=mals_open_buses)

        serializerW = BusSerializers(workingBuses,many=True)
        serializerB = BusSerializers(brokenBuses,many=True)

        return Response({"working":serializerW.data,"broken":serializerB.data})



class Schedules(APIView):
    #permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        #driver = request.GET.get("driver")
        #schedules = Schedule.objects.filter(driver=driver)
        schedules = Schedule.objects.all().order_by('-work_day')
        serializer = ScheduleSerializers(schedules,
                                       many=True)
        return Response({"data":serializer.data})

    def post(self, request):
        #sch = Schedule(bus=self.request.bus)
        schedule = SchedulePostSerializers(data = request.data)
        if schedule.is_valid():
            #schedule.save(driver = request.driver)
            schedule.save()
            return Response({"status":"Add"})
        else:
            return Response(schedule.errors, status=status.HTTP_400_BAD_REQUEST)


class Schedules_detail(APIView):
    #permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return Response({"status":"Delete"})

    def put(self, request, pk):
        sched = Schedule.objects.get(pk=pk)
        serializer = SchedulePutSerializers(sched,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Changed"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Schedules_R(APIView):
    #permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        route = request.GET.get("route")
        schedules = Schedule.objects.filter(route=route)
        serializer = ScheduleSerializers(schedules,
                                       many=True)
        return Response({"data":serializer.data})


class SchedReport(APIView):
    def get(self, request):
        reports = Report.objects.all()
        available = reports.exclude(schedule_line__work_day__gt =
                                    datetime.datetime.today()
                                    ).order_by('-schedule_line__work_day','-schedule_line__work_end')
        next = reports.filter(schedule_line__work_day__gt =
                                    datetime.datetime.today()
                                    ).order_by('schedule_line__work_day','schedule_line__work_end')
        serializer = ReportSerializers(next,many=True)
        serializer2 = ReportSerializers(available, many=True)
        return Response({"next":serializer.data,"available":serializer2.data})


class SchedReport_detail(APIView):
    def put(self, request, pk):
        report = Report.objects.get(pk=pk)
        serializer = ReportPutSerializers(report,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Changed"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
