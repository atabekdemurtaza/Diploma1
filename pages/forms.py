from django import forms 

class ContactForm(forms.Form):

	yourname = forms.CharField(max_length=20, label='Ваше имя')
	email = forms.EmailField(required=False, label='Ваша почта')
	subject = forms.CharField(max_length=100, label='Тема')
	message = forms.CharField(widget=forms.Textarea, label='Сообщение')
	
	