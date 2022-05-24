from django.contrib import admin
from .models import Quote 

class QuoteAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'company', 'submitted', 'quotedate', 'quoteprice')
	list_filter = ('submitted', 'quotedate')
	readonly_fields = ('submitted',)
	fieldsets = (
		(None, {
			'fields': ('name','email','description')
		}),
		('Информаци о пользователе', {
			'classes': ('collapse'),
			'fields' : ('position', 'company', 'address', 'phone', 'web')
		}),
		('Информация о работе', {
			'classes': ('collapse'),
			'fields' : ('sitestatus', 'prioritystatus', 'jobfile', 'submitted')
		}),
		('Панель предложении', {
			'classes': ('collapse'),
			'fields' : ('quotedate','quoteprice','username')
		}),
	)

admin.site.register(Quote, QuoteAdmin)
