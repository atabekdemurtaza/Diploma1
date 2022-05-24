from django.shortcuts import render
from django.http import HttpResponse
from .models import Page 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, get_connection

def index(request, pagename):

	pagename = '/' + pagename 
	#pg = Page.objects.get(permalink=pagename)
	pg = get_object_or_404(Page, permalink=pagename)
	context = {
		'title': pg.title,
		'content': pg.body_text,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all()
	}

	return render(request, 'pages/page.html', context)

def contact(request):

	submitted = False 
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'atabekdemurtaza@gmail.com'),
				['militech.uz'],
				connection = con
			)
			#assert False
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'pages/contact.html', context)