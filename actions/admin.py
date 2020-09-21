from django.contrib import admin
from .models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):


	list_display = ['user' , 'verb' , 'target' , 'created']
	list_filter = ['verb']
	search_fields = ['user']

	
