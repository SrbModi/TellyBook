from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import book_detail, track,req
from check_room.models import check_rooms,rooms, incharge,booked
from check.models import test, dev, prof_contact 
# from datetime import timedelta

# Create your views here.

url="http://192.168.43.204:8000"

#booking details
def input_detail(request):
	if(request.method=="POST"):
		temp= test.objects.get(userid=request.POST.get("userid"))
		temp.reqid=temp.reqid+1
		temp.save()
		book_detail.objects.create(userid=temp.id,
			reqid=temp.reqid,
			eventname=request.POST.get("eventname"),
			eventroom=request.POST.get("eventroom"),
			date= request.POST.get("date"),
			time= request.POST.get("time"),
			condby=request.POST.get("condby"),
			condbyname=request.POST.get("condbyname"),
			desc=request.POST.get("desc"))

		track.objects.create(userid=temp.id,
			reqid=temp.reqid
			)
		o=incharge.objects.get(userid=temp.id)
		req.objects.create(proid=o.profid,userid=o.userid,reqid=temp.reqid)
		return HttpResponse('{"success":"1","message":"Done"}')



#events_list
def events(request):
	if(request.method=="GET"):
		data='{"events":['
		for o in booked.objects.all():
			data+='{"name":"'+str(o.eventname)+'","venue":"'+str(o.eventroom)+'","description":"'+str(o.desc)+'","date":"'+str(o.date)+'","stime":"'+str(o.stime)+'","etime":"'+str(o.etime)+'","image":"'+url+str(o.image.url)+'"},'
		data=data[:-1]
		data+=']}'
		return HttpResponse(data)




#tracking : details - name, designation,message,result
def track_return(request):
	# return HttpResponse('{"track":[{"name":"str(obj1.incharge)","designation":"Faculty-In-Charge","message":"str(obj.message)","result":1},{"name":"Mr. A.P.Rajimwale","designation":"Dean Student Welfare","message":"str(obj.message)","result":1},{"name":"Dr. P.Y. Dhekne","designation":"Registrar","message":"str(obj.message)","result":1},{"name":"str(temp.incharge)","designation":"str(temp.desig)","message":"str(obj.message)","result":1}]}')
	if(request.method=="GET"):
		try:
			obj = track.objects.get(userid=request.GET.get("userid"),reqid=request.GET.get("reqid"))
			obj1= incharge.objects.get(userid=request.GET.get("userid"))
			temp=book_detail.objects.get(userid=request.GET.get("userid"),reqid=request.GET.get("reqid"))
			temp=rooms.objects.get(name=temp.eventroom)
			data = '{"track":[{"name":"'+str(obj1.incharge)+'","designation":"'+'Faculty-In-Charge'+'","message":"'+str(obj.message)+'","result":"'+str(obj.step1)+'"},'
			data+= '{"name":"'+'Mr. A.P.Rajimwale'+'","designation":"'+'Dean Student Welfare'+'","message":"'+str(obj.message)+'","result":"'+str(obj.step2)+'"},'
			data+= '{"name":"'+'Dr. P.Y. Dhekne'+'","designation":"'+'Registrar'+'","message":"'+str(obj.message)+'","result":"'+str(obj.step3)+'"},'
			data+= '{"name":"'+str(temp.incharge)+'","designation":"'+str(temp.desig)+'","message":"'+str(obj.message)+'","result":"'+str(obj.step4)+'"}]}'
			return HttpResponse(data)
		except:
			data = '{"track":[{"name":"'+'Dr. S. Ganguly'+'","designation":"'+'Faculty-In-Charge'+'","message":"'+'str(obj.message)'+'","result":"'+'1'+'"},'
			data+= '{"name":"'+'Mr. A.P.Rajimwale'+'","designation":"'+'Dean Student Welfare'+'","message":"'+'str(obj.message)'+'","result":"'+'1'+'"},'
			data+= '{"name":"'+'Mr.. P.Y. Dhekne'+'","designation":"'+'Registrar'+'","message":"'+'str(obj.message)'+'","result":"'+'0'+'"},'
			data+= '{"name":"'+'Dr. D.S. Sisodia'+'","designation":"'+'HOD CSE Dept.'+'","message":"'+''+'","result":"'+'-2'+'"}]}'
			return HttpResponse(data)


#When the faculty responds to a request
#GET
def on_action(request):
	if(request.method=="GET"):
			try:
				temp=track.objects.get(userid=request.GET.get("userid"),reqid=request.GET.get("reqid"))
				if(request.GET.get("action")=="1"):
					x='step'+str(temp.n)
					temp.x="1"
					temp.save()
				else:
					x='step'+str(temp.n)
					temp.x="-1"
					temp.save()
			except:
				return HttpResponse('{"success":"0","message":"userid and reqid do not match!"')

			if(temp.n!=4):
				temp.n+=1
				temp.save()
				x='step'+str(temp.n)
				temp.x="0"
				temp.save()
				inst = req.objects.get(userid=temp.userid,reqid=temp.reqid)
				if(int(temp.n)==2):
					setattr(inst,"proid","1002") #prof. A.P.Rajimwale
					inst.save()
				elif(int(temp.n)==3):
					setattr(inst,"proid","1003") #Registrar - Dr. D.Y.Dhekene
					inst.save()
				else:
					obj = incharge.objects.get(userid=temp.userid)
					setattr(inst,"proid",obj.profid)
					inst.save()


			else:
				temp = book_detail.objects.get(userid=temp.userid,reqid=temp.reqid)
				o = rooms.objects.get(name=temp.eventroom)
				booked.objects.create(eventname=temp.eventname,eventroom=temp.eventroom,desc=temp.desc,date=temp.date,stime=temp.time,etime=temp.etime,image=o.image.url)


# #When faculty applies for a leave application
# def leave(request):
# 	if(request.method=="GET"):
# 		leave_detail.objects.create(userid=request.GET.get("userid"),
# 			reqid=request.GET.get("reqid"),
# 			sdate=request.GET.get("sdate"),
# 			edate=request.GET.get("edate"),,
# 			reason=request.GET.get("reason"),
# 			desc=request.GET.get("desc"))
		

