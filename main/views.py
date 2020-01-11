from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from . import models, forms

# Create your views here.

class AddArticleView(CreateView):
	#
	# creates a new article
	#
	model = models.BlogArticle
	form_class = forms.AddArticleForm
	template_name = 'add_article.html'
	success_url = '/blog/'

	def form_valid(self, form):
		# add author
		form.instance.author = self.request.user
		# check if premoderation is not required required
		#if self.request.user.groups.filter(Q(name='admins')|Q(name='editors')).exists():
		#	form.instance.status = 1

		return super(AddArticleView, self).form_valid(form)

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

def profile(request):
	# check if comment was posted
	if request.method == 'POST':
		print(request.POST)
		form = forms.UserChangeForm(request.POST, **{'user': request.user})
		if form.is_valid():
			print(form)
	else:
		form = forms.UserChangeForm(**{'user': request.user})
	#print(form)

	return render(
		request=request,
		template_name='profile.html',
		context={'form': form},
		)

def articles_list(request):
	# get list of the articles
	articles = models.BlogArticle.objects.order_by('-posted')
	return render(
		request=request,
		template_name='blog_articles.html',
		context={'articles': articles},
		)

def blog_article(request, article_id):
	# get the article
	article = get_object_or_404(models.BlogArticle, id=article_id)
	
	# check if comment was posted
	if request.method == 'POST':
		print(request.POST)
		form = forms.ArticleCommentForm(request.POST)
		if form.is_valid():
			# create and save the comment
			comment = models.ArticleComment(
				text = form.cleaned_data.get('text'),
				author = request.user,
				article = article,
				)
			comment.save()

	# get the comments
	comments = models.ArticleComment.objects.filter(
		article__id=article_id,
		is_active=True,
		).order_by('-posted')

	return render(
		request=request,
		template_name='blog_article.html',
		context={
			'article': article, 
			'comments':comments,
			'form': forms.ArticleCommentForm,
			},
		)

def site_article(request, section, index):
	# get article
	article = get_object_or_404(models.SiteArticle, section=section, position=index)
	# get associated articles list
	associated = models.BlogArticle.objects.filter(associate_with__id=article.id)
	return render(
		request=request,
		template_name='site_article.html',
		context={
			'article': article,
			'articles': associated,
			},
		)

def group_events(request, group_name):
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
	return group_events(request, 'default')

def event(request, event_id):
	# get the event
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
	comments = models.EventComment.objects.filter(
		event__id=event_id,
		is_active=True,
		).order_by('-posted')

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
