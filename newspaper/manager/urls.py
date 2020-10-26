from django.urls import path,include
from . views import create_paperboy,index,update_paperboy,delete_paperboy
app_name="manager"
urlpatterns = [
	path('',index,name="index"),
	path('create_paperboy/',create_paperboy,name="create_paperboy"),
	path('update_paperboy/<int:id>',update_paperboy,name="update_paperboy"),
	path('delete_paperboy/',delete_paperboy,name="delete_paperboy"),
]