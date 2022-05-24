from django.contrib import admin
from pages.models import Page 

class PageAdmin(admin.ModelAdmin):

	list_display = ('title','update_date')
	search_fields = ('title',)
	ordering = ('title',)

admin.site.register(Page, PageAdmin)
