
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from Employee_app.models import EmployeePersonal,Attendance,EmployeeCareer,EmployeeEucation,Salary,Register,Company,Profiledetail
from django.views import View
from django.contrib.auth import logout
# Create your views here


 
class login(TemplateView):
    template_name = "login.html"

class login_check(APIView,TemplateView):
    template_name = "login.html"

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        try:
            user = Register.objects.get(email=email, password=password)
            role = user.role
            print(role)

            if role in ['employee', 'admin', 'manager']:
                request.session['user'] = email
                request.session['type'] = role

                return JsonResponse({'usertype': role, 'userdetails': email})
            else:
                request.session['user'] = "default"
                request.session['type'] = "default"

                return JsonResponse({'usertype': "default", 'userdetails': email})
        
        except Register.DoesNotExist:
            request.session['user'] = "default"
            request.session['type'] = "default"

            return JsonResponse({'usertype': "default", 'userdetails': {}})
        except Exception as e:
            print(e)  
            return JsonResponse({'usertype': "default", 'userdetails': {}})

def home(request):
    return render(request,'websiteApp/index.html')

def about(request):
    return render(request,'websiteApp/about.html')
def blog(request):
    return render(request,'websiteApp/blog.html')
def contact(request):
    return render(request,'websiteApp/contact.html')
def detail(request):
    return render(request,'websiteApp/detail.html')
def feature(request):
    return render(request,'websiteApp/feature.html')
def price(request):
    return render(request,'websiteApp/price.html')
def quote(request):
    return render(request,'websiteApp/quote.html')
def service(request):
    return render(request,'websiteApp/service.html')
def team(request):
    return render(request,'websiteApp/team.html')
def testimonial(request):
    return render(request,'websiteApp/testimonial.html')
    
