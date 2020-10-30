from rest_framework import serializers
from .models import Flight, AirCarrier, Crew, TransitLanding, Route, Plane, CrewCommander, SecondPilot, Steward, \
    Navigator


class FlightSerializer(serializers.ModelSerializer):
    """"""
    plane = serializers.SlugRelatedField(slug_field="type", read_only=True)
    route = serializers.SlugRelatedField(slug_field="arrival_to", read_only=True)

    class Meta:
        model = Flight
        fields = "__all__"


class TransitLandingSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = TransitLanding
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    """"""
    transit_landing = serializers.SlugRelatedField(slug_field="landing", read_only=True)
    class Meta:
        model = Route
        fields = "__all__"


class PlaneSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Plane
        fields = "__all__"


class CrewCommanderSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = CrewCommander
        fields = "__all__"


class CrewFIOCommanderSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = CrewCommander
        fields = ("last_name", "first_name", "second_name")


class SecondPilotSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = SecondPilot
        fields = "__all__"


class SecondPilotFIOSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = SecondPilot
        fields = ("last_name", "first_name", "second_name")


class StewardSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Steward
        fields = "__all__"


class StewardFIOSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Steward
        fields = ("last_name", "first_name", "second_name")


class NavigatorSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Navigator
        fields = "__all__"


class NavigatorFIOSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Navigator
        fields = ("last_name", "first_name", "second_name")


class CrewSerializer(serializers.ModelSerializer):
    """"""
    crew_commander = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    second_pilot = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    navigator = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    stewards = StewardSerializer(many=True)

    class Meta:
        model = Crew
        fields = "__all__"


class AirCarrierSerializer(serializers.ModelSerializer):
    """"""
    planes = PlaneSerializer(many=True)
    crews = CrewSerializer(many=True)

    class Meta:
        model = AirCarrier
        fields = "__all__"
