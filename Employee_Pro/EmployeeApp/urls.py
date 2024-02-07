from django.urls import path

from EmployeeApp.views import *
from .views import addproduction 
from . import views


urlpatterns = [

    path('',views.index,name='index'),
   
    path('E_profile/',profile.as_view(), name='E_profile'),
    
    
    #---------------employee Personal-----------

    path('changePassword',changePassword.as_view(),name="changePassword"),
    path('updatePassword',updatePassword.as_view(),name="updatePassword"),

    path('Emp_employee_list/', ViewEmployees.as_view(), name='Emp_employee_list'),
    path('get_employee_details', get_employee_details, name='get_employee_details'),

    path('Emp_addemp',E_addemp.as_view(),name='Emp_addemp'),
    path('Emp_employee_list',employee_list.as_view(),name='Emp_employee_list'),
    path('Emp_DeleteEmployee', DeleteEmployee.as_view(), name='Emp_DeleteEmployee'),
    path('Emp_editEmployee/<int:id>/',editEmployee.as_view(),name='Emp_editEmployee'),
    path('Emp_updateEmployee',updateEmployee.as_view(),name="Emp_updateEmployee"),
    #---------------Employee Education------------------------

    path('Emp_employee_list/', ViewEmployeesEducation.as_view(), name='Emp_employee_list'),
    path('get_emp_edu_details', get_emp_edu_details, name='get_emp_edu_details'),

    path('Emp_addemp_education',addemp_education.as_view(),name='Emp_addemp_education'),
    path('Emp_employee_education_list',employee_education_list.as_view(),name='Emp_employee_education_list'),
    path('Emp_DeleteEmployee_education', DeleteEmployee_education.as_view(), name='Emp_DeleteEmployee_education'),
    path('Emp_editEmployeeEducation/<int:id>/',editEmployeeEducation.as_view(),name='Emp_editEmployeeEducation'),
    path('Emp_updateEmployeeEducation',updateEmployeeEducation.as_view(),name="Emp_updateEmployeeEducation"),
    

    #---------------Employee Career------------------------

    path('Emp_employee_list/', ViewEmployeesCareer.as_view(), name='Emp_employee_list'),
    path('get_emp_car_details', get_emp_car_details, name='get_emp_car_details'),

    path('Emp_addemp_career',addemp_career.as_view(),name='Emp_addemp_career'),
    path('Emp_employee_career_list',employee_career_list.as_view(),name='Emp_employee_career_list'),
    path('Emp_DeleteEmployeeCareer', DeleteEmployeeCareer.as_view(), name='Emp_DeleteEmployeeCareer'),
    path('Emp_editEmployeeCareer/<int:id>/',editEmployeeCareer.as_view(),name='Emp_editEmployeeCareer'),
    path('Emp_updateEmployeeCareer',updateEmployeeCareer.as_view(),name="Emp_updateEmployeeCareer"),




    path('Emp_employee_list/', ViewEmployeesAttendance.as_view(), name='Emp_employee_list'),
    path('get_emp_attendance_details', get_emp_attendance_details, name='get_emp_attendance_details'),

    path('Emp_add_attendance',add_attendance.as_view(),name='Emp_add_attendance'),
    path('Emp_attendance_list',attendance_List.as_view(),name='Emp_attendance_list'),
    # path('Deleteattendance',DeleteAttendance.as_view(),name='Deleteattendance'),
    path('Emp_editEmployeeAttendance/<int:id>/',editEmployeeAttendance.as_view(),name='Emp_editEmployeeAttendance'),
    path('Emp_updateEmployeeAttendance',updateEmployeeAttendance.as_view(),name="Emp_updateEmployeeAttendance"),

    
   
     path('production_list/', ViewEmployeeProduction.as_view(), name='production_list'),
    path('get_emp_pro_details', get_emp_pro_details, name='get_emp_pro_details'),
    path('add_production', addproduction.as_view(), name='add_production'),
    path('production_list',production_list.as_view(),name='production_list'),
    path('Deleteproduction', Deleteproduction.as_view(), name='Deleteproduction'),
    path('editEmployeeProduction/<int:id>/',editEmployeeProduction.as_view(),name='editEmployeeProduction'),
    path('updateEmployeeProduction',updateEmployeeProduction.as_view(),name="updateEmployeeProduction"),



    path('addstack', addstack.as_view(), name='addstack'),
    path('stack_list', stack_list.as_view(), name='stack_list'),
    path('ViewEmployeeStack', ViewEmployeeStack.as_view(), name='ViewEmployeeStack'),
    path('get_emp_stack_details', get_emp_stack_details, name='get_emp_stack_details'),
    path('updateEmployeeStack', updateEmployeeStack.as_view(), name='updateEmployeeStack'),
    path('editEmployeeStack/<int:id>/', editEmployeeStack.as_view(), name='editEmployeeStack'),
    path('Deletestack', Deletestack.as_view(), name='Deletestack'),
   

    
    #----------------------Employee Salary-------------------




]