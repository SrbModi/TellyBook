from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import check_rooms,booked,rooms
from check.models import test,logo
from book_detail.models import book_detail,req
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from datetime import timedelta
from pyfcm import FCMNotification

# Create your views here.

url="http://192.168.0.133:8000"
	
# def get_avail(uid,rid):



#booking - requests made && request - requests that needs to be approved
#image - club/commitee ; 
def dash_history(request):
	if(request.method=="GET"):
		count=0
		#usid = int(request.GET.get("userid"))
		usid =request.GET.get("userid")
		print usid
		data='{"historyDatas":['
		if(int(request.GET.get("userid"))<1000):
			for o in book_detail.objects.all():
				print "exec"
				print o.userid
				print usid
				if(int(o.id)==int(usid)):
					print "1"
					#get_avail(int(request.GET.get("userid")),int(request.GET.get("reqid")))
					#data+='{"reqid":"'+str(o.reqid)+'","eventname":"'+str(o.eventname)+'","bdate":"'+str(o.date)+'","eventroom":"'+str(o.eventroom)+'","status":"'+str(o.eventname)+'","status":"'+str(o.eventname)+'","status":"'+str(o.eventname)+'","status":"'+str(o.eventname)+'","status":"'+str(o.eventname)+'","status":"'+str(o.eventname)+'","success":"1","message":"done"},'
					data+='{"reqid":"'+str(o.reqid)+'",'
					data+='"eventname":"'+str(o.eventname)+'",'
					data+='"bdate":"'+str(o.bdate)+'",'
					data+='"eventroom":"'+str(o.eventroom)+'",'
					data+='"status":"'+str(o.status)+'",'
					data+='"time":"'+str(o.time)+'",'
					data+='"cby":"'+str(o.condby)+'",'
					data+='"under":"'+str(o.condbyname)+'",'
					data+='"desc":"'+str(o.desc)+'",'
					#data+='"status":"'+str(o.status)+'",'
					obj = logo.objects.get(name=o.condbyname)
					data+='"image":"'+url+str(obj.image.url)+'",'
					# data+='"success":"1",'
					data+='"message":"done"},'
					count+=1

			if(count>0):
				data=data[:-1]
				data+=']'
			else:
				data+='{"reqid":"'+'0'+'","eventname":"'+'none'+'","bdate":"'+'0'+'","eventroom":"'+'none'+'","status":"'+'0'+'","message":"NO booking request Found"}'
				data+=']'
		else:
			count=0	
			for o in req.objects.all():
				if(o.proid==req.objects.get("userid")):
					# temp=req.objects.get(proid="userid")
					temp=book_detail.objects.get(userid=o.userid,reqid=o.reqid)
					data+='{"reqid":"'+str(temp.reqid)+'",'
					data+='"eventname":"'+str(temp.eventname)+'",'
					data+='"bdate":"'+str(temp.bdate)+'",'
					data+='"eventroom":"'+str(temp.eventroom)+'",'
					data+='"status":"'+str(temp.status)+'",'
					data+='"time":"'+str(temp.time)+'",'
					data+='"cby":"'+str(temp.condby)+'",'
					data+='"under":"'+str(temp.condbyname)+'",'
					data+='"desc":"'+str(temp.desc)+'",'
					obj= logo.objects.get(name=temp.condbyname)
					data+='"image":"'+str(obj.image.url)+'",'
					# data+='"success":"1",'
					data+='"message":"done"},'
					count+=1
				if(count>0):
					data=data[:-1]
					data+=']'
				else:
					data+='{"reqid":"'+'0'+'",'
					data+='"eventname":"'+'none'+'",'
					data+='"bdate":"'+'0'+'",'
					data+='"eventroom":"'+'none'+'",'
					data+='"status":"'+'0'+'",'
					data+='"success":"0",'
					data+='"message":"No Pending Requests"}]'
		
		data+='}'
		return HttpResponse(data)




def noti(request):
	push_service = FCMNotification(api_key="AIzaSyCmH4yxjGRqW_1LX5nQZ0527Hqei0uIWGY")
	registration_id = "dSn3Bmk0j5M:APA91bHB9QAV4gvIrft_z9y6DmjSS-8KZDeknn_6eOfs6bkZZvoDIS7JqnTRqCvCwjzUEkSScScL-R5cp30KFzBxZo1iQETTDgsSvNLE8NLu_4qS_LrrG1qaBnPTSTMhA9Hv6cxivke7"
	message_title = "update"
	message_body = "Hi, your customized feed for today is ready"
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
	return HttpResponse("Done")


# 
# 
# 
# 
#sorting for room suggestion
# 
# 
# 
# 

#to change date by a value j(+/-)
def dateincre(d,j):
	print d[:2]
	print d[3:5]
	print d[6:8]
	dd=int(d[:2])
	mm=int(d[3:5])
	yy=int(d[6:8])
	dd+=j
	if(mm==2):
		if(yy%4==0):
			if(dd>29):
				dd-=29
				mm+=1
			elif(dd<0):
				dd+=31
				mm-=1
		else:
			if(dd>28):
				dd-=28
				mm+=1
			elif(dd<0):
				dd+=31
				mm-=1


	if(mm==4 or mm==6 or mm==9 or mm==11):
		if(dd>30):
			dd-=30
			mm+=1
		elif(dd<0):
			dd+=31
			mm-=1
	else:
		if(dd>31):
			dd-=31
			if(mm==12):
				yy+=1
				mm=1
		elif(dd<0):
			if(mm==1):
				dd+=31
				yy-=1
				mm=12
			else:
				dd+=30
				mm-=1
	if(dd>9):
		if(mm<10):
			val = str(dd)+'-0'+str(mm)+'-'+str(yy)
		else:
			val = str(dd)+'-'+str(mm)+'-'+str(yy)

	else:
		if(mm<10):
			val='0'+str(dd)+'-0'+str(mm)+'-'+str(yy)
		else:
			val = '0'+str(dd)+'-'+str(mm)+'-'+str(yy)



	return val




	






def isbooked(r,d,s,e): #room,date,start,end
	try:
		print "isbooked called"
		obj=booked.objects.get(eventroom=r,date=d)
		stime=float(obj.stime)
		etime=float(obj.etime)
		st=float(s)
		et=float(e)
		print "conversion valid"
		if(etime<=st):
			return 0
		elif(st>=stime):
			if(et<=etime):
				return 0
		elif(et<=stime):
			return 1
		else:
			return 0
	except:
		return 1
#return 0 if not available and 1 if available

#dict = {''}


def date_detail(ro,date1,st,et):
	value=''
	print "date_detail called"
	for i in range(-2,3):
		tempdate = dateincre(date1,i)
		print tempdate
		try:
			temp=booked.objects.get(eventroom=ro,date=tempdate)
			print "booked object found"
			if(i<0):
				strn = 'date_'+str(abs(i))
			else:
				strn = 'date'+str(abs(i))
			print "strn formed as "+strn
			d='"'+strn+'":"'+str(tempdate)+str(isbooked(ro,tempdate,st,et))+'",'
			print "d formed as "+d
		except:
			if(i<0):
				strn = 'date_'+str(abs(i))
			else:
				strn = 'date'+str(abs(i))
			d='"'+strn+'":"'+str(tempdate)+'1'+'",'
		value+=d
	value=value[:-1]
	return(value)






#name, capacity, image, mike, projector, stage, department, available-5()
#false/true values for : 1) mike = 0/1 2)stage : 0/2 3)projector : 0/4
#eventname, date, capacity, stime,etime,proom, floor, mike, stage, projector, 
@csrf_exempt
def roomsugg(request):
	if(request.method =="GET"):
		data = '{"rooms":['
		userid=request.GET.get("userid")
		capacity=request.GET.get("capacity")
		date=request.GET.get("date")
		stime=request.GET.get("stime")
		etime=request.GET.get("etime")
		proom=request.GET.get("proom")
		floor=request.GET.get("floor")
		msp = request.GET.get("msp")
	
		try:
			temp = check_rooms.objects.create(date=date,capacity=capacity,proom=proom,floor=floor,stime=stime,etime=etime)
		except:
			return HttpResponse('{"rooms":[{"eventname":"none","name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+',"success":"0","message":"Wrong default value","image"="http://192.168.0.133:8000/media/FN4_eNYax0J.jpg"}]}')
		

		data='{"rooms":['
		try:
			if(proom!='none'):#android default value for proom = none
				
				try :
					obj=rooms.objects.get(name=proom)	
					data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(obj.name)+'","capacity":"'+str(obj.capacity)+'","mike":"'+str(obj.mike)+'","stage":"'+str(obj.stage)+'","projector":"'+str(obj.projector)+'",'+date_detail(proom,date,stime,etime)+',"image":"'+url+str(obj.image.url)+'","success":"1","message":"Done"},'				
				except:
				 	data+='{"eventname":"none","name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+',"success":"0","message":"Not Done","image"="http://192.168.0.133:8000/media/FN4_eNYax0J.jpg"},'
		
		except:
			data+='{"eventname":"none","name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+',"success":"0","message":"Wrong default value","image"="http://192.168.0.133:8000/media/FN4_eNYax0J.jpg"},'

		# try:
		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==1):
				if(int(o.capacity)>=int(capacity)):
					print "A"
					if(o.msp==msp):
						print "1"
						data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'			
						#continue	
		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==1):
				if(int(o.capacity)<int(capacity)):
					if(o.msp==msp):
						print "2"
						data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+',"success":"1","message":"Done"},'
						#continue
			
		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==1):
				if(int(o.capacity)>=int(capacity)):
					print "3"
					data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'			
					#continue

		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==1):			
				if(int(o.capacity)<int(capacity)):
					print "4"
					data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'
					#continue
		# except:
			#date='{"name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+'","success":"0","message":"msp is wrong"},'

		# try:
		for o in rooms.objects.all():
			print o.name
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==0):
				print "block B called"
				if(o.capacity>=capacity):
					if(o.msp==msp):
						data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'
					continue

		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==0):
				if(o.capacity>=capacity):
					data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'
					continue

		for o in rooms.objects.all():
			if(o.name!=proom and isbooked(o.name,date,stime,etime)==0):
				if(o.capacity<capacity):
					data+='{"eventname":"'+str(request.GET.get("eventroom"))+'","name":"'+str(o.name)+'","capacity":"'+str(o.capacity)+'","mike":"'+str(o.mike)+'","stage":"'+str(o.stage)+'","projector":"'+str(o.projector)+'","department":"'+str(o.depart)+'",'+date_detail(o.name,date,stime,etime)+',"image":"'+url+str(o.image.url)+'","success":"1","message":"Done"},'
					continue
	# except:
	# 		data+='{"name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+'","success":"0","message":"data is wrong"},'

	# try:

		data=data[:-1]
		data+=']}'
		# except:
		# 	data='{"name":"None","capacity":"'+'none'+'","mike":"'+'none'+'","stage":"'+'none'+'","projector":"'+'none'+'"date_1":"0","date_2":"0","date0":"0","date1":"0","date2":"0"'+'","success":"0","message":"Failure"},'
		
		
		return HttpResponse(data)
					



#return function for display of available chioces 