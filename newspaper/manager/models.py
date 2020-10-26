from django.db import models
from django.contrib.auth import get_user_model

from newsadmin.models import Branch
User=get_user_model()
# Create your models here.

class Manager(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="manager",blank=True,null=True)
	branch = models.OneToOneField(Branch,on_delete=models.CASCADE,related_name="branch_manager")
	manager_name = models.CharField(max_length=120)

	def __str__(self):
		return "{} manager of {} branch ".format(self.manager_name,self.branch.name)
