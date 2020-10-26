from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import render,redirect
def role_required(allowed_roles=[]):
	def decorator(view_func):
		def wrap(request, *args, **kwargs):
			# print(request.user.user_type)
			if request.user.is_authenticated:
				if request.user.user_type in allowed_roles:
					return view_func(request, *args, **kwargs)
				else:
					return render(request,"404.html",{'home_page_url':reverse(request.user.user_type+":index")})
			else:
				return redirect('accounts:login')
		return wrap
	return decorator