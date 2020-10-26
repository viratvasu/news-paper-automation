from django.db import models
from newsadmin.models import Branch
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
# from enduser.models import UserProfile
class PaperBoyManager(models.Manager):
	def get_paper_boy(self,pincode=None):
		paper_boy_obj=PaperBoy.objects.filter(pincode__iexact=pincode)
		if not paper_boy_obj:
			greaterthan_paper_boy_queryset 	    = PaperBoy.objects.filter(pincode__gt=pincode).first()
			lessthan_paper_boy_queryset 		= PaperBoy.objects.filter(pincode__lt=pincode).last()
			if greaterthan_paper_boy_queryset and lessthan_paper_boy_queryset:
				if abs(greaterthan_paper_boy_queryset.pincode-pincode) < abs(lessthan_paper_boy_queryset.pincode-pincode):
					return greaterthan_paper_boy_queryset
				else:
					return lessthan_paper_boy_queryset
			else:
				if lessthan_paper_boy_queryset:
					return lessthan_paper_boy_queryset
				else:
					return greaterthan_paper_boy_queryset
		return paper_boy_obj
class PaperBoy(models.Model):
	user    = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name="paperboy")
	branch  = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
	name 	= models.CharField(max_length=200)
	pno 	= models.CharField(max_length=10)
	pincode = models.IntegerField(default=524341)
	objects 	= PaperBoyManager()
	def __str__(self):
		return self.name
class DeliveryStatus(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
	present_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10,default="Deliveried")
# I want to become web developer.I am good at back-end and front-end .I have done some projects already in different streams.I am good in HTML,CSS,BOOTSTRAP,JavaScript,J query,Ajax,Django.I am having good knowledge in tech startups,so i can help them by giving ideas and suggestions