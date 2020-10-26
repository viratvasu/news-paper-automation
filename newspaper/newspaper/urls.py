"""newspaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enduser import views
from newsadmin.views import create_branch
from django.conf import settings
from django.conf.urls.static import static
from manager.views import create_paperboy
urlpatterns = [
    path('admin1/', admin.site.urls),
    path('',include('enduser.urls')),
    path('user/',include('accounts.urls')),
    path('admin/',include('newsadmin.urls')),
    path('manager/',include('manager.urls')),
    path('paperboy/',include('paperboy.urls')),
    # path('',views.signup,name="signup"),
    # path('index/',views.index,name="index"),
    # path('modify_news_papers_subscription/<int:id>',views.modify_news_papers_subscription,name="modify_news_papers_subscription"),
    # path('branch/',create_branch),
    # path('create_paperboy/',create_paperboy)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)