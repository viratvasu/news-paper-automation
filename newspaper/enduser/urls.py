from django.urls import path
from .views import index,signup,modify_news_papers_subscription,modify_magazines_subscription
app_name="enduser"

urlpatterns = [
	path('',index,name="index"),
	path('signup/',signup,name="signup"),
	path('modify_news_papers_subscription/',modify_news_papers_subscription,name="modify_news_papers_subscription"),
	path('modify_magazines_subscription/<int:id>',modify_magazines_subscription,name="modify_magazines_subscription"),
]