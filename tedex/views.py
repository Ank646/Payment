from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt

from .models import ticket

# Create your views here.
client = razorpay.Client(auth=("rzp_test_f3KO9cFrfsZwpG", "8XOiUSGqoxjHwQTQRKdXBkEv"))
       
def index(request):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        mobile=request.POST['mno']
        college=request.POST['coll']
        obj=ticket.objects.create(nme=name,email=email,college=college,phone=mobile)
        obj.save()
        currency= "INR"
        orderr=client.order.create({'amount':50000,'currency':currency,'payment_capture':1})
        order_id=orderr['id']
        
        h={
            'name':name,
            'email':email,
            'mob':mobile
        }
        
        return render(request,"index.html",{'name':name,'email':email,'mob':mobile})
    else:

        return render(request,'index.html')
@csrf_exempt
def success(request):
    return render(request,"main.html")    