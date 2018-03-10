from django.contrib import admin

# Register your models here.

from models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
	list_display = [
	'title',
	'desc',
	'location',
	]


admin.site.register(Complaint,ComplaintAdmin)
