from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'slug', 'store', 'status')
	list_display_links = ('id', 'slug')
	search_fields = ('slug',)
	fields = ('status', 'slug', 'store')
	readonly_fields = ('store', 'slug')


admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
