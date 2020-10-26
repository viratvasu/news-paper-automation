from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from newsadmin.models import NewsPaper,Magazine
from accounts.forms import UserCreationForm
from paperboy.models import PaperBoy
from .forms import UserProfileForm
from .models import Subscription
from django.http import JsonResponse
User=get_user_model()
from newspaper.decorators import role_required
def index(request):
	user_prof=[]
	prof_sub=[]
	if request.user.is_authenticated and request.user.user_type=="enduser":
		user_prof 	= request.user.user_profile
		prof_sub 	= Subscription.objects.new_or_get(request,user_prof)
	elif request.user.is_authenticated:
		return redirect(request.user.user_type+":index")
	news_papers = NewsPaper.objects.all()
	magazines = Magazine.objects.all()
	return render(request,'enduser/index.html',{'news_papers':news_papers,'magazines':magazines,'user_subscriptions':prof_sub})
def signup(request):
	if request.user.is_authenticated:
		messages.success(request, "You can't access this page while logged in..")
		return redirect('enduser:index')
	if request.POST:
		form = UserCreationForm(request.POST)
		pform=UserProfileForm(request.POST)
		if form.is_valid() and pform.is_valid():
			user_obj 			= form.save()
			user_prof 			= pform.save(commit=False)
			user_prof.user 		= user_obj
			user_pincode 		= request.POST.get('pincode')
			paper_boy_obj   	= PaperBoy.objects.get_paper_boy(user_pincode)
			user_prof.paper_boy	= paper_boy_obj
			user_prof.save()
			messages.success(request, "Account Created successfully...Login")
			return redirect('accounts:login')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
			errors = pform.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form=UserCreationForm()
	pform=UserProfileForm()
	return render(request,'enduser/signup.html',{'form':form,'pform':pform})
def modify_news_papers_subscription(request):
	if request.user.is_authenticated and request.user.user_type=="enduser":
		prof_sub=Subscription.objects.new_or_get(request,request.user.user_profile)
		news_paper_obj=NewsPaper.objects.get(id=request.POST.get("id"))
		if news_paper_obj in prof_sub.news_papers.all():
			prof_sub.news_papers.remove(news_paper_obj)
			return JsonResponse({'message':'Add to Subscription'})
		else:
			prof_sub.news_papers.add(news_paper_obj)
			return JsonResponse({'message':'Remove From Subscription'})
	else:
		if request.user.is_authenticated:
			return JsonResponse({'url':reverse(request.user.user_type+":index")},status=400)
		else:
			return JsonResponse({'url':reverse('accounts:login')},status=400)
@role_required(allowed_roles=['enduser'])
def modify_magazines_subscription(request,id):
	if request.user.is_authenticated and request.user.user_type=="enduser":
		prof_sub=Subscription.objects.new_or_get(request,request.user.user_profile)
		magazine_obj=Magazine.objects.get(id=id)
		if magazine_obj in prof_sub.magazines.all():
			prof_sub.magazines.remove(magazine_obj)
			return JsonResponse({'message':'Add to Subscription'})
		else:
			prof_sub.magazines.add(magazine_obj)
			return JsonResponse({'message':'Remove From Subscription'})
	else:
		if request.user.is_authenticated:
			return JsonResponse({'url':reverse(request.user.user_type+":index")},status=400)
		else:
			return JsonResponse({'url':reverse('accounts:login')},status=400)