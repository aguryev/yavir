from django import forms
from . import models


class EventCommentForm(forms.ModelForm):
	#
	# form to comment an event
	#
	text = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '3',
		'placeholder': 'Напішить свійй коментарій',
		}))


	class Meta:
		model = models.EventComment
		fields = ['text']