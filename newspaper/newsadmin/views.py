from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from manager.forms import ManagerForm
from accounts.forms import UserCreationForm
from .forms import BranchForm,NewsPaperForm,MagazineForm
from . models import Branch,NewsPaper,Magazine
from newspaper.decorators import role_required
# Create your views here.
@role_required(allowed_roles=['newsadmin'])
def index(request):
	availabel_branches 		= Branch.objects.all()
	available_news_papers 	= NewsPaper.objects.all()
	available_magazines 	= Magazine.objects.all()
	return render(request,'newsadmin/index.html',{'availabel_branches':availabel_branches,'available_news_papers':available_news_papers,'available_magazines':available_magazines})

@role_required(allowed_roles=['newsadmin'])
def create_branch(request):
	if request.method == "POST":
		form 	= BranchForm(request.POST)
		mform  	= ManagerForm(request.POST)
		uform   = UserCreationForm(request.POST)
		if form.is_valid() and mform.is_valid() and uform.is_valid():
			user_obj 			= uform.save()
			user_obj.user_type  = "manager"
			user_obj.save()
			branch_obj 			= form.save()
			manger_obj 			= mform.save(commit=False)
			manger_obj.branch 	= branch_obj
			manger_obj.user 	= user_obj
			manger_obj.save()
			messages.success(request, "Branch created successfully")
			return redirect('newsadmin:index')
		else:
			errors = uform.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)

			errors = mform.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)

			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= BranchForm()
	uform   = UserCreationForm()
	mform  	= ManagerForm()
	return render(request,'newsadmin/create_branch.html',{'form':form,'mform':mform,'uform':uform,'theme':'Add'})
@role_required(allowed_roles=['newsadmin'])
def update_branch(request,id):
	branch_instance  = get_object_or_404(Branch,id=id)
	manager_instance = branch_instance.branch_manager
	if request.method == "POST":
		form 	= BranchForm(request.POST,instance=branch_instance)
		mform  	= ManagerForm(request.POST,instance=manager_instance)
		if form.is_valid() and mform.is_valid():
			branch_obj 			= form.save()
			manger_obj 			= mform.save()
			messages.success(request, "Branch Updated successfully")
			return redirect('newsadmin:index')
		else:
			errors = mform.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)

			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= BranchForm(instance=branch_instance)
	mform  	= ManagerForm(instance=manager_instance)
	return render(request,'newsadmin/create_branch.html',{'form':form,'mform':mform,'theme':'Update'})
@role_required(allowed_roles=['newsadmin'])
def delete_branch(request):
	branch_instance  = get_object_or_404(Branch,id=request.POST.get("id"))
	if branch_instance:
		branch_instance.delete()
		messages.success(request, "Branch Deleted successfully")
	return JsonResponse({'message':'Deleted Sucessfully'})
@role_required(allowed_roles=['newsadmin'])
def create_newsPaper(request):
	if request.method == "POST":
		form 	= NewsPaperForm(request.POST,request.FILES)
		if form.is_valid():
			news_paper_obj=form.save()
			messages.success(request, "News Paper created successfully")
			return redirect('newsadmin:index')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= NewsPaperForm()
	return render(request,'newsadmin/create.html',{'form':form,'theme':'News Paper','theme1':'add'})

@role_required(allowed_roles=['newsadmin'])
def update_newsPaper(request,id):
	news_paper_instance=get_object_or_404(NewsPaper,id=id)
	if request.method == "POST":
		form 	= NewsPaperForm(request.POST,request.FILES,instance=news_paper_instance)
		if form.is_valid():
			news_paper_obj=form.save()
			messages.success(request, "News Paper Updated successfully")
			return redirect('newsadmin:index')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= NewsPaperForm(instance=news_paper_instance)
	return render(request,'newsadmin/create.html',{'form':form,'theme':'News Paper','theme1':'update'})
@role_required(allowed_roles=['newsadmin'])
def delete_newsPaper(request):
	news_paper_instance  = get_object_or_404(NewsPaper,id=request.POST.get("id"))
	if news_paper_instance:
		news_paper_instance.delete()
		messages.success(request, "News Paper Deleted successfully")
	return JsonResponse({'message':'Deleted Sucessfully'})
@role_required(allowed_roles=['newsadmin'])
def create_magazine(request):
	if request.method == "POST":
		form 	= MagazineForm(request.POST,request.FILES)
		if form.is_valid():
			magazine_obj = form.save()
			messages.success(request, "Magazine created successfully")
			return redirect('newsadmin:index')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= MagazineForm()
	return render(request,'newsadmin/create.html',{'form':form,'theme':'Magazine','theme1':'add'})

@role_required(allowed_roles=['newsadmin'])
def update_magazine(request,id):
	magazine_instance=get_object_or_404(Magazine,id=id)
	if request.method == "POST":
		form 	= MagazineForm(request.POST,request.FILES,instance=magazine_instance)
		if form.is_valid():
			magazine_obj = form.save()
			messages.success(request, "Magazine created successfully")
			return redirect('newsadmin:index')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= MagazineForm(instance=magazine_instance)
	return render(request,'newsadmin/create.html',{'form':form,'theme':'Magazine','theme1':'update'})

@role_required(allowed_roles=['newsadmin'])
def delete_magazine(request):
	magazine_instance  = get_object_or_404(Magazine,id=request.POST.get("id"))
	if magazine_instance:
		magazine_instance.delete()
		messages.success(request, "Magazine Deleted successfully")
	return JsonResponse({'message':'Deleted Sucessfully'})