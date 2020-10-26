from django.shortcuts import render
from .models import PaperBoy
from newspaper.decorators import role_required
# Create your views here.
@role_required(allowed_roles=['paperboy'])
def index(request):
	pb 					= request.user.paperboy
	delivery_details 	= pb.paper_boy.all()
	return render(request,'paperboy/index.html',{'delivery_details':delivery_details})