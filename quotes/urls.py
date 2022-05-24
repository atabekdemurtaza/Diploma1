from django.urls import path 
from .views import quote_req
from .views import QuoteList
from .views import QuoteView

urlpatterns = [
	path('', quote_req, name='quote_request'),
	path('show/<int:pk>', QuoteView.as_view(), name='quote-detail'),
	path('show', QuoteList.as_view(), name='show-quotes'),
]