from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello Django!")
def index(request):
    return render(request,"index.html")

#登录动作
def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if username == 'admin' and password == 'admin123' :
			response = HttpResponseRedirect('/event_manage/')
			response.set_cookie('user', username, 3600) #添加浏览器cookie
			return response

#发布会管理
def event_manage(request):
	username = request.COOKIES.get('user', '') #读取浏览器cookie
	return render(request, "event_manage.html", {"user":username})