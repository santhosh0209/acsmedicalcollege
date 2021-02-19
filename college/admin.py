from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import New,Event,Department,Achievement,best_moments,Awards,HOD,Professor,Facility,Gallery
from django.db import models

admin.site.register(New)  

admin.site.register(Event)  

class MeasurementMethodAdmin(admin.ModelAdmin):
  def has_module_permission(self, request):
    return False

class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 1

class BestMomentInline(admin.StackedInline):
    model = best_moments
    extra = 3

class AwardsInline(admin.StackedInline):
    model = Awards
    extra = 1
class HODInline(admin.StackedInline):
    model = HOD
    extra = 1
class ProfessorInline(admin.StackedInline):
    model = Professor
    extra = 1
class FacilityInline(admin.StackedInline):
    model = Facility
    extra = 1
class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    inlines = [AchievementInline,BestMomentInline,AwardsInline,HODInline,ProfessorInline,FacilityInline,GalleryInline]

admin.site.register(Department, PersonAdmin)
admin.site.register(Achievement,MeasurementMethodAdmin)
admin.site.register(best_moments,MeasurementMethodAdmin)
admin.site.register(Awards,MeasurementMethodAdmin)
admin.site.register(HOD,MeasurementMethodAdmin)
admin.site.register(Professor,MeasurementMethodAdmin)
admin.site.register(Facility,MeasurementMethodAdmin)
admin.site.register(Gallery,MeasurementMethodAdmin)
