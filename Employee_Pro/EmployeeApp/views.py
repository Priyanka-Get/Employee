from django.http import JsonResponse
from django.shortcuts import get_object_or_404,redirect,render
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from Employee_app.models import EmployeePersonal,Attendance,EmployeeCareer,EmployeeEucation,Salary,Register,Company
from django.views import View
from EmployeeApp.models import Production, Stack 


# Create your views here.
def index(request):
    E_count = EmployeePersonal.objects.count()
    C_count = Company.objects.count()

    context = {
        'E_count': E_count,
        'C_count': C_count
    }
   
    return render(request,'EmployeeApp/index.html', context)



class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'EmployeeApp/changepassword.html'

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
        return redirect("/login_check")    
#Personal Details
class E_addemp(TemplateView,APIView):
    template_name = "EmployeeApp/addemp.html"
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
    template_name = "EmployeeApp/employee_list.html"

# ---------------popup-----------------
    
class ViewEmployees(TemplateView):
    template_name = 'EmployeeApp/employee_list.html'

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
    template_name = 'EmployeeApp/editemp.html'
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
    template_name = "EmployeeApp/addemp_education.html"

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
    template_name = 'EmployeeApp/employee_education_list.html' 
    
class DeleteEmployee_education(View):
    def get(self, request):
        empedu_id = request.GET.get('empedu_id', None)
        EmployeeEucation.objects.get(empedu_id=empedu_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)  
            
class editEmployeeEducation(TemplateView):
    template_name = 'EmployeeApp/editemp_education.html'
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
    template_name = 'EmployeeApp/employee_education_list.html'

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
    template_name = "EmployeeApp/addemp_career.html"

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
    template_name = 'EmployeeApp/employeecareer_list.html'


class DeleteEmployeeCareer(View):
    def get(self, request):
        empcar_id = request.GET.get('empcar_id', None)
        EmployeeCareer.objects.get(empcar_id=empcar_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data) 


class editEmployeeCareer(TemplateView):
    template_name = 'EmployeeApp/editemp_career.html'
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
    template_name = 'EmployeeApp/employeecareer_list.html'

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
    template_name = 'EmployeeApp/add_attendance.html'

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
    template_name = 'EmployeeApp/attendance_list.html'


# class DeleteAttendance(View):
#     def get(self, request):
#         attendance_id = request.GET.get('attendance_id', None)
#         Attendance.objects.get(attendance_id=attendance_id).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)

class editEmployeeAttendance(TemplateView):
    template_name = 'EmployeeApp/editemp_attendance.html'
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
    template_name = 'EmployeeApp/attendance_list.html'

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
 




  
              
class addproduction(TemplateView,APIView):

    template_name = "EmployeeApp/addproduction.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context
    
    def post(self, request):
        emp_id = request.POST['emp_id']
        product_id = request.POST['product_id']
        production_date = request.POST['production_date']
        shift = request.POST['shift']
        quantity_produced = request.POST['quantity_produced']
        work_center = request.POST['work_center']
        production_order_id = request.POST['production_order_id']
        time_in = request.POST['time_in']
        time_out = request.POST['time_out']
        production_status = request.POST['production_status']

        try: 
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
            
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'})    
        production_instance = Production(
            employee=employee_instance,
            product_id=product_id,
            production_date=production_date,
            shift=shift,
            quantity_produced=quantity_produced,
            work_center=work_center,
            production_order_id=production_order_id,
            time_in=time_in,
            time_out=time_out,
            production_status=production_status
)
        production_instance.save()
        return JsonResponse({'status': 'Success'})  

class production_list(ListView):
    model = Production
    template_name = 'EmployeeApp/production_list.html'


class Deleteproduction(View):
    def get(self, request):
        production_id = request.GET.get('production_id', None)
        Production.objects.get(production_id=production_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class editEmployeeProduction(TemplateView):
    template_name = 'EmployeeApp/editproduction.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            # context['id'] = self.kwargs['id']
            alist = Production.objects.filter(production_id=kwargs['id'])
        except:
            alist = Production.objects.filter(production_id=context['id'])
            
        context={'plist':list(plist),'alist':list(alist)}
        return context
    

class updateEmployeeProduction(APIView):
   
    def post(self, request):
        production_id = request.POST['production_id']
        
        emp_id = request.POST['employee']
        product_id = request.POST['product_id']
        production_date = request.POST['production_date']
        shift = request.POST['shift']
        quantity_produced = request.POST['quantity_produced']
        work_center = request.POST['work_center']
        production_order_id = request.POST['production_order_id']
        time_in = request.POST['time_in']
        time_out = request.POST['time_out']
        production_status = request.POST['production_status']
        
       

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        production_instance=get_object_or_404(Production,production_id=production_id)
        production_instance.employee=personal_instance
        production_instance.product_id=product_id
        production_instance.production_date = production_date
        production_instance.shift=shift
        production_instance.quantity_produced=quantity_produced
        production_instance.work_center=work_center
        production_instance.production_order_id=production_order_id
        production_instance.time_out=time_out
        production_instance.time_in=time_in

        production_instance.production_status=production_status

       
        production_instance.save()
        return JsonResponse({'success': True}, status=200)   



        #-------------popup form--------------------------------- 
    
class ViewEmployeeProduction(TemplateView):
    template_name = 'EmployeeApp/production_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Production.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_pro_details(request):
    production_id = request.GET.get('production_id')
    employee_production = Production.objects.get(production_id=production_id)

    data = {
            'first_name': employee_production.employee.first_name,
            'last_name': employee_production.employee.last_name,
            'product_id':employee_production.product_id,
            'production_date':employee_production.production_date,
            'shift':employee_production.shift,
            'quantity_produced':employee_production.quantity_produced,
            'work_center':employee_production.work_center,
            'production_order_id':employee_production.production_order_id,
            'time_in':employee_production.time_in,
            'time_out':employee_production.time_out,
            'production_status':employee_production.production_status
        
    }
    return JsonResponse(data)        
       
class addstack(TemplateView,APIView):
    template_name = "EmployeeApp/addstack.html"  # Replace with the actual template name
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_list = EmployeePersonal.objects.all()
        context['employee_list'] = employee_list
        return context
    
    def post(self, request):
        # Process the POST request data
        emp_id = request.POST['emp_id']
        product_id = request.POST['product_id']
        stack_date = request.POST['stack_date']
        stack_quantity = request.POST['stack_quantity']
        stack_location = request.POST['stack_location']
        stack_order_id = request.POST['stack_order_id']
        stack_notes = request.POST['stack_notes']

        
        try: 
            employee_instance = EmployeePersonal.objects.get(pk=emp_id)
            
        except EmployeePersonal.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'Invalid category ID'}) 

        # Create a new Stack instance
        stack_instance  = Stack(
            employee=employee_instance ,
            product_id=product_id,
            stack_date=stack_date,
            stack_quantity=stack_quantity,
            stack_location=stack_location,
            stack_order_id=stack_order_id,
            stack_notes=stack_notes
        )

        stack_instance .save()

        return JsonResponse({'status': 'Success'})

class stack_list(ListView):
    model=Stack
    template_name = "EmployeeApp/stack_list.html"

class Deletestack(View):
    def get(self, request):
        stack_id = request.GET.get('stack_id', None)
        Stack.objects.get(stack_id=stack_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class editEmployeeStack(TemplateView):
    template_name = 'EmployeeApp/edit_Stack.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plist=EmployeePersonal.objects.all()

        try:
            # context['id'] = self.kwargs['id']
            alist = Stack.objects.filter(stack_id=kwargs['id'])
        except:
            alist = Stack.objects.filter(stack_id=context['id'])
            
        context={'plist':list(plist),'alist':list(alist)}
        return context
    

class updateEmployeeStack(APIView):
   
    def post(self, request):
        stack_id = request.POST['stack_id']
        
        emp_id = request.POST['employee']
        product_id = request.POST['product_id']
        stack_date = request.POST['stack_date']
       
        stack_location = request.POST['stack_location']
        stack_notes = request.POST['stack_notes']
        stack_order_id = request.POST['stack_order_id']
        stack_quantity = request.POST['stack_quantity']
       
       

        personal_instance = get_object_or_404(EmployeePersonal,emp_id=emp_id)
        
        stack_instance=get_object_or_404(Production,stack_id=stack_id)
        stack_instance.employee=personal_instance
        stack_instance.product_id=product_id
        stack_instance.stack_date = stack_date
        stack_instance.stack_location=stack_location
        stack_instance.stack_notes=stack_notes
        stack_instance.stack_order_id=stack_order_id
        stack_instance.stack_quantity=stack_quantity
        

       

       
        stack_instance.save()
        return JsonResponse({'success': True}, status=200)   



        #-------------popup form--------------------------------- 
    
class ViewEmployeeStack(TemplateView):
    template_name = 'EmployeeApp/stack_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Stack.objects.all()  # Fix typo in model name
        context['object_list'] = employees
        return context

def get_emp_stack_details(request):
    stack_id = request.GET.get('stack_id')
    employee_stack = Stack.objects.get(stack_id=stack_id)

    data = {
            'first_name': employee_stack.employee.first_name,
            'last_name': employee_stack.employee.last_name,
            'product_id':employee_stack.product_id,
            'stack_date':employee_stack.stack_date,
            'stack_quantity':employee_stack.stack_quantity,
            'stack_notes':employee_stack.stack_notes,
            'stack_location':employee_stack.stack_location,
            'stack_order_id':employee_stack.stack_order_id,
            
        
    }
    return JsonResponse(data) 

class profile(TemplateView):
    """
    Render feature map template
    """
    template_name = 'EmployeeApp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reglist = Register.objects.all()
        context = {'reglist': list(reglist)}
        return context
