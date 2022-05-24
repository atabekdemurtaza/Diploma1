from django.db import models
from django.contrib.auth.models import User 
from phone_field import PhoneField

STATUS_CHOICES = (
	('Новый', 'Новый сайт'),
	('Действующий', 'Действующий сайт')
)

PRIORITY_CHOICES = (
	('Н', 'Недавно - 1 неделя или меньше'),
	('С', 'Средний - 2 или 4 недели'),
	('Д', 'Дольше  - Не действительный')
)

class Quote(models.Model):

	name = models.CharField('Название', max_length=60)
	position = models.CharField('Положение', max_length=100, blank=True)
	company = models.CharField('Место работы', max_length=100, blank=True)
	address = models.CharField('Место жительство', max_length=100, blank=True)
	phone = PhoneField('Телефон', blank=True, help_text='Номер телефона')
	email = models.EmailField('Почта')
	web = models.URLField('Ссылка', blank=True)
	description = models.TextField('Описание')
	sitestatus = models.CharField('Статус', choices=STATUS_CHOICES, max_length=20)
	prioritystatus = models.CharField('Приоритет', choices=PRIORITY_CHOICES, max_length=20)
	jobfile = models.FileField('Файл', upload_to='uploads/', blank=True)
	submitted = models.DateField('Представлен', auto_now_add=True)
	quotedate = models.DateField('Дата предложения', blank=True, null=True)
	quoteprice = models.DecimalField('Цена', decimal_places=2, max_digits=7, blank=True, default=0)
	username = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.CASCADE)

	class Meta:

		verbose_name_plural = 'Предложения'
		verbose_name = 'Предложении'

	def __str__(self):

		return self.name







