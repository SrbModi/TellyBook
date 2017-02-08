from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import test,dev,prof_contact
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

url="http://192.168.43.204:8000"

def check_add(request):
	test.objects.create(username = request.POST.get("username"),password=request.POST.get("password"))
	return HttpResponse("Done (y)")

def check_return(request):
	if(request.method=="POST"):
		temp = get_object_or_404(test, username = request.POST.get("username"))
		data = '{"detail":[{"username":"'+str(temp.username)+'","password":"'+str(temp.password)+'"}]}'
	return HttpResponse(data)

@csrf_exempt 
def check_verify(request):
	if(request.method=="POST"):
		#try:
		temp=test.objects.get(username = request.POST.get("username"))
		#temp = get_object_or_404(test, username = request.POST.get("username"))
		if(temp.password==request.POST.get("password")):
			return HttpResponse('{"success":"'+'true'+'","message":"'+'Verified'+'","id":"'+str(int(temp.userid))+'"}')
		else:
			return HttpResponse('{"success":"'+'false'+'","message":"'+'Not Verified'+'","id":0}')
	#except:
			#return HttpResponse('{"success":"'+'false'+'","message":"'+'user not found'+'","id":0}')
	else:
		return render(request,"test.html")


def dev_detail(request):
	if(request.method=="GET"):
		data='{"dev":['
		for o in dev.objects.all():
			data+='{"name":"'+str(o.name)+'",'
			data+='"branch":"'+str(o.branch)+'",'
			data+='"sem":"'+str(o.sem)+'",'
			data+='"phone":"'+str(o.phone)+'",'
			data+='"email":"'+str(o.email)+'",'
			data+='"linkedin":"'+str(o.linkedin)+'"},'
		data=data[:-1]
		data+=']}'
		return HttpResponse(data)

def profcontact(request):
	if(request.method=="GET"):
		if(request.method=="GET"):
			data='{"contacts":['
			for o in prof_contact.objects.all():
				data+='{"name":"'+str(o.name)+'",'
				data+='"desig":"'+str(o.desig)+'",'
				data+='"phone":"'+str(o.phone)+'",'
				data+='"image":"'+url+str(o.image.url)+'"},'
			data=data[:-1]
			data+=']}'
			return HttpResponse(data)



def imagetest(request):
	temp=prof_contact.objects.get(name="Dr. A.M. Rawani")
	data=temp.image.url
	return HttpResponse(data)

import requests
def test_fcm(request):
	print "1"
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	"Content-Type":"application/json",
	"Authorization":"Key=AIzaSyBe9zJ8AzhwYKUGrjwpnXZcCO3DCSiG7Cc"
	}
	print "2"
	data={ "to" : "dSn3Bmk0j5M:APA91bHB9QAV4gvIrft_z9y6DmjSS-8KZDeknn_6eOfs6bkZZvoDIS7JqnTRqCvCwjzUEkSScScL-R5cp30KFzBxZo1iQETTDgsSvNLE8NLu_4qS_LrrG1qaBnPTSTMhA9Hv6cxivke7",
	"notification": {"title": "Check Tilte","body": "Check Body"}
	}
	#intent-Id
	print "3"
  	print data
	return HttpResponse(requests.request('POST',url,headers=headers,data=data))