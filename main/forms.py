from django import forms
from . import models


class UserChangeForm(forms.ModelForm):
	#
	# form to change user profile data
	#
	children = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '3',
		'placeholder': 'Напішить свій коментар',
		}))

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(UserChangeForm, self).__init__(*args, **kwargs)
		if user is not None:
			self.fields['first_name'].value = 'user.first_name'
			#self.last_name = user.last_name
		#print('***************************** self')
		#print(self.fields['first_name'].value)

	class Meta:
		model = models.User
		fields = ['first_name', 'last_name']

class AddArticleForm(forms.ModelForm):
	#
	# form for adding a new article to blog
	#
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': "Назва (обов'язково)",
		}))
	brief = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control',
			'rows': '3',
			'placeholder': 'Короткий опис',
			}),
		required=False,
		)
	text = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '10',
		'placeholder': "Текст статті (обовязково)",
		}))
	#associate_with = forms.CharField(widget=forms.Select(attrs={
	#	'class': 'form-control',
	#	'placeholder': "Прив'язати до...",
	#	}))

	class Meta:
		model = models.BlogArticle
		fields = ['title', 'brief', 'text', 'image', 'associate_with']

class ArticleCommentForm(forms.ModelForm):
	#
	# form to comment an article
	#
	text = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '3',
		'placeholder': 'Напішить свій коментар',
		}))


	class Meta:
		model = models.EventComment
		fields = ['text']

class EventCommentForm(forms.ModelForm):
	#
	# form to comment an event
	#
	text = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '3',
		'placeholder': 'Напішить свій коментар',
		}))


	class Meta:
		model = models.EventComment
		fields = ['text']