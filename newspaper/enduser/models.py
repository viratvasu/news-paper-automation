from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from newsadmin.models import NewsPaper,Magazine
from paperboy.models import PaperBoy
User=get_user_model()

class UserProfile(models.Model):
    paper_boy  = models.ForeignKey(PaperBoy,on_delete=models.CASCADE,related_name="paper_boy",null=True,blank=True)
    user       = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    name       = models.CharField(max_length=200)
    pno        = models.CharField(max_length=10)
    door_num   = models.CharField(max_length=200,default="0-0-0-0")
    village    = models.CharField(max_length=200,default="chittaluru")
    mandal     = models.CharField(max_length=200,default="chejerla")
    pincode    = models.IntegerField(default=524341)

    def get_papers(self):
        return self.profile_subscription.news_papers.all()
    def get_magazines(self):
        today=datetime.now()
        if today.strftime("%a")=="Sun" and today.strftime("%-d")=="1":
            all_magazines=self.profile_subscription.magazines.all()
        elif today.strftime("%a")=="Sun":
            all_magazines=self.profile_subscription.magazines.filter(magazine_type__iexact="weekly")
        elif today.strftime("%-d")=="1":
            all_magazines=self.profile_subscription.magazines.filter(magazine_type__iexact="monthly")
        else:
            all_magazines=[]
        return all_magazines
    def __str__(self):
    	return self.name
class SubscriptionManager(models.Manager):
    def new_or_get(self,request,pro_obj):
        try:
        	subscription_obj = Subscription.objects.get(profile=pro_obj)
        except Exception:
        	subscription_obj = None
        if subscription_obj:
        	return subscription_obj
        else:
        	print("Not fount subscriptions...creating your subscriptions")
        	subscription_obj=Subscription(profile=pro_obj)
        	subscription_obj.save()
        return subscription_obj
class Subscription(models.Model):
	profile 	= models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="profile_subscription")
	news_papers = models.ManyToManyField(NewsPaper)
	magazines 	= models.ManyToManyField(Magazine)
	objects 	= SubscriptionManager()

	def __str__(self):
		return self.profile.name