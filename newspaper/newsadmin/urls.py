
from django.urls import path
from .views import create_branch,create_newsPaper,create_magazine,index,update_branch,update_newsPaper,update_magazine,delete_branch,delete_magazine,delete_newsPaper
app_name="newsadmin"
urlpatterns = [
	path('',index,name="index"),
	path('create_branch/',create_branch,name="create_branch"),
	path('update_branch/<int:id>',update_branch,name="update_branch"),
	path('delete_branch/',delete_branch,name="delete_branch"),
	path('create_newsPaper/',create_newsPaper,name="create_newsPaper"),
	path('update_newsPaper/<int:id>',update_newsPaper,name="update_newsPaper"),
	path('delete_newsPaper/',delete_newsPaper,name="delete_newsPaper"),
	path('create_magazine/',create_magazine,name="create_magazine"),
	path('update_magazine/<int:id>',update_magazine,name="update_magazine"),
	path('delete_magazine/',delete_magazine,name="delete_magazine"),
	
]