from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages 
from accounts.forms import UserCreationForm
from paperboy.forms import PaperBoyForm
from paperboy.models import PaperBoy
from newspaper.decorators import role_required
# Create your views here.
@role_required(allowed_roles=['manager'])
def index(request):
	available_paperboys = PaperBoy.objects.all()
	return render(request,'manager/index.html',{'available_paperboys':available_paperboys})

@role_required(allowed_roles=['manager'])
def create_paperboy(request):
	if request.method=="POST":
		form    	= PaperBoyForm(request.POST)
		uform   	= UserCreationForm(request.POST)
		branch_obj 	= request.user.manager.branch
		if form.is_valid() and uform.is_valid():
			user_obj 				= uform.save(commit=False)
			user_obj.user_type 		= 'paperboy'
			user_obj.save()
			paper_boy_obj 			= form.save(commit=False)
			paper_boy_obj.branch 	= branch_obj
			paper_boy_obj.user 		= user_obj
			paper_boy_obj.save()
			messages.success(request, "PaperBoy created successfully")
			return redirect('manager:index')
		else:
			errors = uform.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)

			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= PaperBoyForm()
	uform   = UserCreationForm()
	return render(request,'manager/create.html',{'form':form,'uform':uform,'theme':'Add'})
@role_required(allowed_roles=['manager'])
def update_paperboy(request):
	paper_boy_instance = PaperBoy.objects.get(id=request.POST.get("id"))
	if request.method=="POST":
		form    	= PaperBoyForm(request.POST,instance=paper_boy_instance)
		if form.is_valid():
			paper_boy_obj = form.save()
			messages.success(request, "PaperBoy Updated successfully")
			return redirect('manager:index')
		else:
			errors = form.errors.as_data()
			for key in errors:
				error_list = errors[key][0]
				for i in error_list:
					messages.success(request, i)
	form 	= PaperBoyForm(instance=paper_boy_instance)
	return render(request,'manager/create.html',{'form':form,'theme':'Update'})

@role_required(allowed_roles=['manager'])
def delete_paperboy(request):
	paper_boy_instance  = get_object_or_404(PaperBoy,id=request.POST.get("id"))
	if paper_boy_instance:
		paper_boy_instance.delete()
		messages.success(request, "PaperBoy Deleted successfully")
	return JsonResponse({'message':'Deleted Sucessfully'})