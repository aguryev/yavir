from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from . import models, forms

# Create your views here.

def home(request):
	#classes = models.ClassDescription.objects.all()
	articles = models.SiteArticle.objects.filter(section='0').order_by('position')
	classes = models.SiteArticle.objects.filter(section='1').order_by('position')
	return render(
		request=request,
		template_name='home.html',
		context={
			'articles': articles, 
			'classes': classes,
			}
		)

def site_article(request, section, index):
	article = get_object_or_404(models.SiteArticle, section=section, position=index)
	return render(
		request=request,
		template_name='site_article.html',
		context={'article': article},
		)

def events_list(request, group_name):
	if group_name == 'default' or request.user.groups.filter(name=group_name).exists():
		events = models.Event.objects.filter(group__name=group_name).order_by('-time_start')
		return render(
			request=request,
			template_name='events_list.html',
			context={'events': events},
			)
	else:
		return redirect('main:home')

def default_events(request):
	return events_list(request, 'default')

def event(request, event_id):
	# grt the event
	event = get_object_or_404(models.Event, id=event_id)

	# check if comment was posted
	if request.method == 'POST':
		print(request.POST)
		form = forms.EventCommentForm(request.POST)
		if form.is_valid():
			# create and save the comment
			comment = models.EventComment(
				text = form.cleaned_data.get('text'),
				author = request.user,
				event = event,
				)
			comment.save()

	# get the comments
	comments = models.EventComment.objects.filter(event__id=event_id).order_by('-posted')

	return render(
		request=request,
		template_name='event.html',
		context={
			'event': event, 
			'comments': comments,
			'form': forms.EventCommentForm,
			}
		)

def info(request, group_name):
	persons = models.KeyPerson.objects.filter(group__name=group_name)
	return render(
		request=request,
		template_name='info.html',
		context={'group': group_name, 'persons': persons},
		)

def schedule(request, group_name):
	#persons = models.KeyPerson.objects.filter(group__name=group_name)
	lessons_sorted = models.Lesson.objects.filter(group__name=group_name).order_by('end_time', 'start_time')
	week = {}
	for lesson in lessons_sorted:
		lesson_time_span = lesson.get_time_span()
		if not lesson_time_span in week:
			week[lesson_time_span] = ['', '', '', '', '']
		week[lesson_time_span][lesson.get_day_int()-1] = lesson.title
	return render(
		request=request,
		template_name='schedule.html',
		context={'group': group_name, 'week':week},
		)

def privacypolicy(request):
	return render(
		request=request,
		template_name='privacypolicy.html',
		context={},
		) 