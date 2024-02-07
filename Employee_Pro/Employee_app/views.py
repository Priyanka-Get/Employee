from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from Employee_app.models import EmployeePersonal,Attendance,EmployeeCareer,EmployeeEucation,Salary,Register,Company,Profiledetail
from django.views import View
from django.contrib.auth import logout

# Create your views here.


def index(request):
    E_count = EmployeePersonal.objects.count()
    C_count = Company.objects.count()

    context = {
        'E_count': E_count,
        'C_count': C_count
    }
   
    return render(request,'Employee_app/index.html', context)


# class index(TemplateView):
#     E_count = EmployeePersonal.objects.count()
#     C_count = Company.objects.count()

#     context = {
#         'E_count': E_count,
#         'C_count': C_count
#     }
#     # template_name = "Employee_app/index.html"
#     return render(request,'Employee_app/index.html', context)


class forgot(TemplateView):
    template_name = "forgot.html"  

   

class employee_list(ListView):
    model= EmployeePersonal
    template_name = "Employee_app/employee_list.html"

# ---------------popup-----------------
    
class ViewRegister(TemplateView):
    template_name = 'Employee_app/register_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Register.objects.all()
        context['object_list'] = employees
        return context  
   

def get_reg_details(request):
    id = request.GET.get('id')
    employee = Register.objects.get(id=id)
    data = {
        'email': employee.email,
        'password': employee.password,
        'confirm_password': str(employee.confirm_password),
        'role': employee.role,
        
    }
    return JsonResponse(data)    




def logout_view(request):
    logout(request)
    return redirect('/E_login_check') 
 
class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'Employee_app/changepassword.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reglist = Register.objects.all()
        context = {'reglist': list(reglist)}
        return context
class updatePassword(APIView):
   
    def post(self, request):
       
        password = request.POST['pass']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']

        Register.objects.filter(email=email).update(password=password,confirm_password=confirm_password)
        return redirect("/E_login_check")
    
class PasswordResetView(TemplateView):
    template_name = "password_reset.html"

    def post(self, request):
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the email and other requirements (you can add more validation)

        # For simplicity, assuming the email is valid, update the password
        try:
            user = Register.objects.get(email=email)
            user.password = new_password
            user.save()
            return JsonResponse({'status': 'success', 'message': 'Password reset successfully'})
        except Register.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'No user found with the provided email'})

from django.contrib import messages

class sign_in(TemplateView, APIView):
    template_name = "Employee_app/register.html"

    def post(self, request):
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if role == "" or email == "" or password == "" or confirm_password == "":
            return JsonResponse({'status': "fail", 'reason': 'All fields are mandatory'})

        # Validate password criteria
        if len(password) < 8 or not any(char.isdigit() for char in password) \
                or not any(char.isupper() for char in password) \
                or not any(char.islower() for char in password) \
                or not any(char in '!@#$%^&*()-_=+[]{}|;:\'",.<>/?' for char in password):
            messages.error(request, 'Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters.')
            return redirect('register')  # Replace 'your_register_url_name' with the actual URL name for your register page

        # Check if password and confirm password match
        if password != confirm_password:
            messages.error(request, 'Password and confirm password do not match.')
            return redirect('register')  # Replace 'your_register_url_name' with the actual URL name for your register page

        # Save user details to the database
        user = Register(email=email, password=password, confirm_password=confirm_password, role=role)
        user.save()

        return JsonResponse({'status': 'Success'})

        


#Personal Details
class E_addemp(TemplateView,APIView):
    template_name = "Employee_app/addemp.html"
    def post(self , request):
        print(request)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        address = request.POST['address']
        phno = request.POST['phno']
        email = request.POST['email']
        adhar_no = request.POST['adhar_no']
        pan_no = request.POST['pan_no']
        if first_name == '' or last_name =='' or dob == '' or address == '' or phno== '' or email== '' or adhar_no == '' or pan_no == ''  :
            return JsonResponse({'status':"fail","reason":"email and pass mandatory"})
        else:
            user = EmployeePersonal()
            user.first_name = first_name
            user.last_name = last_name
            user.dob =dob
            user.address = address
            user.phno = phno
            user.email=email
            user.adhar_no = adhar_no
            user.pan_no = pan_no
            user.save()
            return JsonResponse({'status':"Success"})

class employee_list(ListView):
    model= EmployeePersonal
    template_name = "Employee_app/employee_list.html"

# ---------------popup-----------------
    
class ViewEmployees(TemplateView):
    template_name = 'Employee_app/employee_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = EmployeePersonal.objects.all()
        context['object_list'] = employees
        return context  
   

def get_employee_details(request):
    emp_id = request.GET.get('emp_id')
    employee = EmployeePersonal.objects.get(emp_id=emp_id)
    data = {
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'dob': str(employee.dob),
        'address': employee.address,
        'phno': employee.phno,
        'email': employee.email,
        'adhar_no': employee.adhar_no,
        'pan_no': employee.pan_no,
    }
    return JsonResponse(data)
  

class DeleteEmployee(View):
    def get(self, request):
        emp_id = request.GET.get('emp_id', None)
        EmployeePersonal.objects.get(emp_id=emp_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
class editEmployee(TemplateView):
    template_name = 'Employee_app/editemp.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['id'] = self.kwargs['id']
            elist = EmployeePersonal.objects.filter(emp_id=context['id'])
        except:
            elist = EmployeePersonal.objects.filter(emp_id=context['id'])
            
        context['elist']= list(elist)
        return context

class updateEmployee(APIView):
   
    def post(self, request):
        emp_id = request.POST['emp_id']
        first_name = request.POST['first_name']
       
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        address = request.POST['address']
        phno= request.POST['phno']
        email = request.POST['email']
        adhar_no = request.POST['adhar_no']
        pan_no = request.POST['pan_no']

       
        employee=EmployeePersonal.objects.get(emp_id=emp_id)
        employee.first_name=first_name
        employee.last_name = last_name
        employee.dob= dob
        employee.address = address
        employee.phno = phno
        employee.email = email
        employee.adhar_no = adhar_no
        employee.pan_no = pan_no
       
        employee.save()
        return JsonResponse({'success': True}, status=200)


    # Employee Eduacation
class addemp_education(TemplateView,APIView):
    template_name = "Employee_app/addemp_education.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context
    def post(self , request):
        print(request)
      

        emp_id = request.POST['emp_id']
        class_name = request.POST['class_name']
        university = request.POST['university']
        percentage = request.POST['percentage']
        pass_out = request.POST['pass_out']
     
        try: 
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
            
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'})    
        education_instance = EmployeeEucation(employee=employee_instance,class_name=class_name,university=university,pass_out=pass_out,percentage=percentage)
        education_instance.save()
        return JsonResponse({'status': 'Success'})   
    
class employee_education_list(ListView):
    model = EmployeeEucation
    template_name = 'Employee_app/employee_education_list.html' 
    
class DeleteEmployee_education(View):
    def get(self, request):
        empedu_id = request.GET.get('empedu_id', None)
        EmployeeEucation.objects.get(empedu_id=empedu_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)  
            
class editEmployeeEducation(TemplateView):
    template_name = 'Employee_app/editemp_education.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            context['id'] = self.kwargs['id']
            elist = EmployeeEucation.objects.filter(empedu_id=context['id'])
        except:
            elist = EmployeeEucation.objects.filter(empedu_id=context['id'])
            
        context={'plist':list(plist),'elist':list(elist)}
        return context

class updateEmployeeEducation(APIView):
   
    def post(self, request):
        empedu_id = request.POST['empedu_id']
        emp_id = request.POST['employee']
        class_name= request.POST['class_name']
        university = request.POST['university']
       
        percentage = request.POST['percentage']
        pass_out = request.POST['pass_out']
       

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        education_instance=get_object_or_404(EmployeeEucation,empedu_id=empedu_id)
        education_instance.employee=personal_instance
        education_instance.class_name=class_name
        education_instance.university = university
        education_instance.percentage= percentage
        education_instance.pass_out = pass_out
        education_instance.save()
        return JsonResponse({'success': True}, status=200)

        #-------------popup form--------------------------------- 
    
class ViewEmployeesEducation(TemplateView):
    template_name = 'Employee_app/employee_education_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = EmployeeEucation.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_edu_details(request):
    empedu_id = request.GET.get('empedu_id')
    employee_education = EmployeeEucation.objects.get(empedu_id=empedu_id)

    data = {
        'first_name': employee_education.employee.first_name,
        'last_name': employee_education.employee.last_name,
        'class_name': employee_education.class_name,
        'university': str(employee_education.university),
        'percentage': employee_education.percentage,
        'pass_out': employee_education.pass_out,
    }
    return JsonResponse(data)
  
    
class addemp_career(TemplateView,APIView):
    template_name = "Employee_app/addemp_career.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context
    
    def post(self , request):
        print(request)
      

        emp_id = request.POST['emp_id']
        company_name = request.POST['company_name']
        title = request.POST['title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        try: 
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
            
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'})    
        career_instance = EmployeeCareer(employee=employee_instance,company_name=company_name,title=title,start_date=start_date,end_date=end_date)
        career_instance.save()
        return JsonResponse({'status': 'Success'})  
           
class employee_career_list(ListView):
    model = EmployeeCareer
    template_name = 'Employee_app/employeecareer_list.html'


class DeleteEmployeeCareer(View):
    def get(self, request):
        empcar_id = request.GET.get('empcar_id', None)
        EmployeeCareer.objects.get(empcar_id=empcar_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data) 


class editEmployeeCareer(TemplateView):
    template_name = 'Employee_app/editemp_career.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            context['id'] = self.kwargs['id']
            elist = EmployeeCareer.objects.filter(empcar_id=context['id'])
        except:
            elist = EmployeeCareer.objects.filter(empcar_id=context['id'])
            
        context={'plist':list(plist),'elist':list(elist)}
        return context

class updateEmployeeCareer(APIView):
   
    def post(self, request):
        empcar_id = request.POST['empcar_id']
        emp_id = request.POST['employee']
        company_name= request.POST['company_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        title = request.POST['title']
       

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        career_instance=get_object_or_404(EmployeeCareer,empcar_id=empcar_id)
        career_instance.employee=personal_instance
        career_instance.company_name=company_name
        career_instance.start_date = start_date
        career_instance.end_date= end_date
        career_instance.title = title
        career_instance.save()
        return JsonResponse({'success': True}, status=200)       


        #-------------popup form--------------------------------- 
    
class ViewEmployeesCareer(TemplateView):
    template_name = 'Employee_app/employeecareer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = EmployeeCareer.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_car_details(request):
    empcar_id = request.GET.get('empcar_id')
    employee_career = EmployeeCareer.objects.get(empcar_id=empcar_id)

    data = {
        'first_name': employee_career.employee.first_name,
        'last_name': employee_career.employee.last_name,
        'company_name': employee_career.company_name,
        'title': str(employee_career.title),
        'start_date': employee_career.start_date,
        'end_date': employee_career.end_date,
    }
    return JsonResponse(data)
  

class add_attendance(TemplateView,APIView):
    template_name = 'Employee_app/add_attendance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context


    def post(self, request):
        emp_id= request.POST['emp_id']
       
       
        status = request.POST['status']
       
        try: 
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
            
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'})    
        attendance_instance = Attendance(employee=employee_instance,status=status)
        attendance_instance.save()
        return JsonResponse({'status': 'Success'})
        
class attendance_List(ListView):
    model = Attendance
    template_name = 'Employee_app/attendance_list.html'


# class DeleteAttendance(View):
#     def get(self, request):
#         attendance_id = request.GET.get('attendance_id', None)
#         Attendance.objects.get(attendance_id=attendance_id).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)

class editEmployeeAttendance(TemplateView):
    template_name = 'Employee_app/editemp_attendance.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            # context['id'] = self.kwargs['id']
            alist = Attendance.objects.filter(attendance_id=kwargs['id'])
        except:
            alist = Attendance.objects.filter(attendance_id=context['id'])
            
        context={'plist':list(plist),'alist':list(alist)}
        return context
    

class updateEmployeeAttendance(APIView):
   
    def post(self, request):
        
        emp_id = request.POST['employee']
        attendance_id = request.POST['attendance_id']
        date= request.POST['date']
        status = request.POST['status']
        
       

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        attendance_instance=get_object_or_404(Attendance,attendance_id=attendance_id)
        attendance_instance.employee=personal_instance
        attendance_instance.date=date
        attendance_instance.status = status
       
        attendance_instance.save()
        return JsonResponse({'success': True}, status=200)   



        #-------------popup form--------------------------------- 
    
class ViewEmployeesAttendance(TemplateView):
    template_name = 'Employee_app/attendance_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Attendance.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_attendance_details(request):
    attendance_id = request.GET.get('attendance_id')
    employee_attendance = Attendance.objects.get(attendance_id=attendance_id)

    data = {
        'first_name': employee_attendance.employee.first_name,
        'last_name': employee_attendance.employee.last_name,
        'date': str(employee_attendance.date),
        'status': employee_attendance.status,
        
    }
    return JsonResponse(data)            

        
class add_salary(TemplateView,APIView):
    template_name = "Employee_app/add_salary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context
    
    def post(self, request, *args, **kwargs):
        emp_id = request.POST.get('emp_id')
        base_salary = float(request.POST.get('base_salary', 0))
        allowance = float(request.POST.get('allowance', 0))
        hra = float(request.POST.get('hra', 0))
        bonus = float(request.POST.get('bonus', 0))

        try:
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid employee ID'})

        ctc = base_salary + allowance + hra + bonus

        # Create and save the Salary instance
        salary_instance = Salary(
            employee=employee_instance,
            base_salary=base_salary,
            allowance=allowance,
            hra=hra,
            bonus=bonus,
            ctc=ctc
        )
        salary_instance.save()

        return JsonResponse({'status': 'Success'}) 
    



           
class salary_list(ListView):
    model = Salary
    template_name = 'Employee_app/salary_list.html'


class DeleteEmployeeSalary(View):
    def get(self, request):
        sal_id = request.GET.get('sal_id', None)
        Salary.objects.get(sal_id=sal_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)  

class editEmployeeSalary(TemplateView):
    template_name = 'Employee_app/editemp_salary.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            context['id'] = self.kwargs['id']
            elist = Salary.objects.filter(sal_id=context['id'])
        except:
            elist = Salary.objects.filter(sal_id=context['id'])
            
        context={'plist':list(plist),'elist':list(elist)}
        return context

class updateEmployeeSalary(APIView):
   
    def post(self, request):
        emp_id = request.POST.get('employee')
        sal_id = request.POST.get('sal_id')
        base_salary = float(request.POST.get('base_salary', 0))
        allowance = float(request.POST.get('allowance', 0))
        hra = float(request.POST.get('hra', 0))
        bonus = float(request.POST.get('bonus', 0))
       
        ctc = base_salary + allowance + hra + bonus

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        salary_instance=get_object_or_404(Salary,sal_id=sal_id)
        salary_instance.employee=personal_instance
        salary_instance.base_salary=base_salary
        salary_instance.hra = hra
        salary_instance.allowance= allowance
        salary_instance.bonus = bonus
        salary_instance.ctc = ctc
        salary_instance.save()
        return JsonResponse({'success': True}, status=200)   
        
class ViewEmployeeSalary(TemplateView):
    template_name = 'Employee_app/salary_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Salary.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_sal_details(request):
    sal_id = request.GET.get('sal_id')
    employee_salary = Salary.objects.get(sal_id=sal_id)

    data = {
        'first_name': employee_salary.employee.first_name,
        'last_name': employee_salary .employee.last_name,
        'base_salary': employee_salary .base_salary,
        'hra': str(employee_salary .hra),
        'allowance': employee_salary .allowance,
        'bonus': employee_salary .bonus,
        'ctc':employee_salary .ctc,
    }
    return JsonResponse(data)
  
#Personal Details
class addcomp(TemplateView,APIView):
    template_name = "Employee_app/addcomp.html"
    def post(self , request):
        print(request)
        cName = request.POST['cName']
        cEmail = request.POST['cEmail']
        cUrl = request.POST['cUrl']
        cAddress = request.POST['cAddress']
        cPhno = request.POST['cPhno']
        
        if cName == '' or cEmail =='' or cUrl == '' or cAddress == '' or cPhno == ''   :
            return JsonResponse({'status':"fail","reason":"email and pass mandatory"})
        else:
            user = Company()
            user.cName = cName
            user.cEmail = cEmail
            user.cUrl = cUrl
            user.cPhno = cPhno
            user.cAddress=cAddress
            user.save()
            return JsonResponse({'status':"Success"})

class comp_list(ListView):
    model= Company
    template_name = "Employee_app/comp_list.html"  

# ---------------popup-----------------
    
class ViewCompany(TemplateView):
    template_name = 'Employee_app/comp_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.all()
        context['object_list'] = company
        return context  
   

def get_company_details(request):
    comp_id = request.GET.get('comp_id')
    company = Company.objects.get(comp_id=comp_id)
    data = {
        'cName': company.cName,
        'cEmail': company.cEmail,
        'cAddress': str(company.cAddress),
        'cUrl': company.cUrl,
        'cPhno': company.cPhno,
       
    }
    return JsonResponse(data)
  

class DeleteCompany(View):
    def get(self, request):
        comp_id = request.GET.get('comp_id', None)
        Company.objects.get(comp_id=comp_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
class editCompany(TemplateView):
    template_name = 'Employee_app/edit_comp.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['id'] = self.kwargs['id']
            elist = Company.objects.filter(comp_id=context['id'])
        except:
            elist = Company.objects.filter(comp_id=context['id'])
            
        context['elist']= list(elist)
        return context

class updateCompany(APIView):
   
    def post(self, request):
        comp_id = request.POST['comp_id']
        cName = request.POST['cName']
       
        cEmail = request.POST['cEmail']
        cAddress = request.POST['cAddress']
        cPhno = request.POST['cPhno']
        cUrl = request.POST['cUrl']

       
        employee=Company.objects.get(comp_id=comp_id)
        employee.cName=cName
        employee.cEmail = cEmail
        employee.cUrl= cUrl
        employee.cAddress = cAddress
        employee.cPhno = cPhno
       
        employee.save()
        return JsonResponse({'success': True}, status=200)




def profiledetail(request, emp_id):
    # Fetch the specific employee details
    employee = get_object_or_404(EmployeePersonal, emp_id=emp_id)

    # Fetch related data for the specific employee
    education = EmployeeEucation.objects.filter(employee=employee)
    career = EmployeeCareer.objects.filter(employee=employee)
    attendance = Attendance.objects.filter(employee=employee)
    salary = Salary.objects.filter(employee=employee).first()  # Assuming each employee has one salary record

    # Pass the employee data to the HTML template
    context = {
        'employee': employee,
        'education': education,
        'career': career,
        'attendance': attendance,
        'salary': salary,
    }
    return render(request, 'Employee_App/profiledetail.html', context)





class profile(TemplateView):
    """
    Render feature map template
    """
    template_name = 'Employee_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reglist = Register.objects.all()
        context = {'reglist': list(reglist)}
        return context





class profile_list(ListView):
    model= EmployeePersonal
    template_name = "Employee_app/profile_list.html"         