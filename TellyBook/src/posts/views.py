from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.mail import send_mail
from book_detail.models import track
from check.models import test
# from datetime import timedelta
from pyfcm import FCMNotification


# Create your views here.
def posts_home(request):
	return HttpResponse('['+'{'+'"a"' +':'+'"first"'+'}'+']') 

def start(request):
	return HttpResponse("hello")

def posts_create(request):
	queryset=Post.objects.all()
	context={
	"object_list": queryset,
	"title": "list"
	}
	return render(request, "index.html",context)
	#return HttpResponse("<h1>create</h1>") 

def posts_detail(request, id=None ):
	instance = get_object_or_404(Post, id = id)
	context = {
	"instance":instance,
	"title":instance.title
	}
	return render(request,"details.html",context) 

def posts_list(request):
	if(request.method=="POST"):
		temp = get_object_or_404(Post, title=request.POST.get("otitle"))
		setattr(temp,"title",request.POST.get("ntitle"))
		temp.save()
	return render(request, "test.html",{})

def send(temp):
	return HttpResponse('[' + '{' + '"title"' + ':"' + str(temp.title) +'",' + '"content"' + ':"' + str(temp.content) + '",' + '"id"' + ':"' + str(temp.id) + '"' + '}' + ']')

def posts_return(request):
	if(request.method=="POST"):
		temp1 = Post.objects.get(title=request.POST.get("title"),content=request.POST.get("content"))
		return send(temp1)
	return render(request, "test1.html",{}) 

def posts_update(request):
	temp=Post.objects.get(title="first")
	temp.content="twice edited content"
	print temp.content
	temp.save()
	return HttpResponse("done")




def posts_delete(request):
	#if(request.method=="POST"):	
	proxy_dict = {
          "http"  : "http://192.168.43.204:8000/$",
          #"https" : "http://192.168.0.133:8000",
        }

	push_service = FCMNotification(api_key="AIzaSyAPhyuQT7UbmKC2PNF6NPDFhNZ6AB5E8UI",proxy_dict=proxy_dict)
	registration_id = request.GET.get("fcm")
	message_title = "Uber update"
	message_body = "Hi john, your customized news for today is ready"
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
	# st = "done,"
	# st=st[:-1]

	# temp = Post.objects.get(title="Title1")
	# temp.date += timedelta(days=1)
	# temp.save()
	return HttpResponse("Done")



