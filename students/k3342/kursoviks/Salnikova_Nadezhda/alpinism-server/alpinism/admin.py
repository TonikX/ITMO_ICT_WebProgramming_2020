from django.contrib import admin
from alpinism.models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
    list_display_links = ('id', 'country_name')


class MountainAdmin(admin.ModelAdmin):
    list_display = ('mountain_name', 'country', 'region', 'height')
    list_display_links = ('mountain_name', 'country', 'region', 'height')


class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'country', 'city', 'contact_person', 'email', 'telephone')
    list_display_links = ('club_name', 'country', 'city', 'contact_person', 'email', 'telephone')


class AlpinistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'club_name', 'telephone', 'email', 'address')
    # list_display_links = ('name', 'birth_date', 'club_name', 'telephone', 'email', 'address')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_code', 'all_participant', 'contact_person', 'email', 'telephone', 'group_success')
    # list_display_links = ('group_code', 'participant', 'contact_person', 'email', 'telephone', 'group_success')

    def all_participant(self, obj):
        return ",\n".join([alpinist.name for alpinist in obj.participant.all()])


class IndSuccessAdmin(admin.ModelAdmin):
    list_display = ('group', 'participant', 'individual_success')
    list_display_links = ('group', 'participant', 'individual_success')


class AscentAdmin(admin.ModelAdmin):
    list_display = ('ascent_code', 'group', 'mountain', 'duration', 'complexity', 'ascent_height', 'start_date', 'end_date')
    list_display_links = ('ascent_code', 'group', 'duration', 'complexity', 'ascent_height', 'start_date', 'end_date')


class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('participant', 'ascent', 'date', 'situation', 'commentary')
    list_display_links = ('participant', 'ascent', 'date', 'situation', 'commentary')


admin.site.register(Country, CountryAdmin)
admin.site.register(Mountain, MountainAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Alpinist, AlpinistAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(IndSuccess, IndSuccessAdmin)
admin.site.register(Ascent, AscentAdmin)
admin.site.register(Emergency, EmergencyAdmin)
