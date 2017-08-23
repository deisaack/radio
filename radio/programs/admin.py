from django.contrib import admin
from . models import Day, Program, Staff, Time, Event



class TimeInline(admin.TabularInline):
    model = Time
    extra = 0
    # radio_fields = {'day': admin.VERTICAL}


class ProgramAdmin(admin.ModelAdmin):
    inlines = [
        TimeInline
           ]
    filter_horizontal = ['presenters']
    list_display = ('title', 'created')
    empty_value_display = 'unknown'
    search_fields = ['title',]

    class Meta:
        model = Program



admin.site.register(Program, ProgramAdmin)

# class TimeInline(admin.StackedInline):
#     model = Time
#
#
# class NewProgramAdmin(Program):
#     inlines = [TimeInline]
#     list_display = ('title', 'description', 'start', 'duration',
#                     )

# admin.site.register(Program, NewProgramAdmin)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'staff_no', 'gender']
    search_fields = ['user__email']

admin.site.register(Staff, StaffAdmin)
admin.site.register(Event)

class OccationInline(admin.TabularInline):
    model = Time.day.through
    extra = 0

class DayAdmin(admin.ModelAdmin):
    inlines = [
        OccationInline,
    ]

class GroupAdmin(admin.ModelAdmin):
    inlines = [
        OccationInline,
    ]
    exclude = ('day',)

admin.site.register(Time, GroupAdmin)
admin.site.register(Day, DayAdmin)

