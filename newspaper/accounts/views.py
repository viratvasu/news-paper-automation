from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def login_user(request):
	if request.user.is_authenticated:
		messages.success(request, "You cannot access this page while looged in")
		return redirect(request.user.user_type+":index")
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			messages.success(request, "Looged In as "+user.email+" Succesfully")
			return redirect(user.user_type+":index")
		else:
			print("I think credentials incorrect")
	return render(request,'accounts/login.html')

def logout_user(request):
	logout(request)
	return redirect("enduser:index")