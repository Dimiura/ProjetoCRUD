from django.contrib import admin
from pilots.models import Pilot, Team

class PilotAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'age', 'team')
    search_fields = ('name', 'team')


admin.site.register(Pilot, PilotAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'namet', )
    search_fields = ('namet', )


admin.site.register(Team, TeamAdmin)