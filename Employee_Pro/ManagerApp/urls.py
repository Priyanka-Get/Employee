from django.urls import path

from ManagerApp.views import *
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('E_profile',profile.as_view(),name='E_profile'),
 
   
    path('Emp_changePassword',changePassword.as_view(),name="Emp_changePassword"),
    path('Emp_updatePassword',updatePassword.as_view(),name="Emp_updatePassword"),
    
    #---------------employee Personal-----------

    path('employee_list/', ViewEmployees.as_view(), name='employee_list'),
    path('get_employee_details', get_employee_details, name='get_employee_details'),

    path('addemp',addemp.as_view(),name='addemp'),
    path('employee_list',employee_list.as_view(),name='employee_list'),
    path('DeleteEmployee', DeleteEmployee.as_view(), name='DeleteEmployee'),
    path('editEmployee/<int:id>/',editEmployee.as_view(),name='editEmployee'),
    path('updateEmployee',updateEmployee.as_view(),name="updateEmployee"),

    #---------------Employee Education------------------------

    path('employee_list/', ViewEmployeesEducation.as_view(), name='employee_list'),
    path('get_emp_edu_details', get_emp_edu_details, name='get_emp_edu_details'),

    path('addemp_education',addemp_education.as_view(),name='addemp_education'),
    path('employee_education_list',employee_education_list.as_view(),name='employee_education_list'),
    path('DeleteEmployee_education', DeleteEmployee_education.as_view(), name='DeleteEmployee_education'),
    path('editEmployeeEducation/<int:id>/',editEmployeeEducation.as_view(),name='editEmployeeEducation'),
    path('updateEmployeeEducation',updateEmployeeEducation.as_view(),name="updateEmployeeEducation"),
    

    #---------------Employee Career------------------------

    path('employee_list/', ViewEmployeesCareer.as_view(), name='employee_list'),
    path('get_emp_car_details', get_emp_car_details, name='get_emp_car_details'),

    path('addemp_career',addemp_career.as_view(),name='addemp_career'),
    path('employee_career_list',employee_career_list.as_view(),name='employee_career_list'),
    path('DeleteEmployeeCareer', DeleteEmployeeCareer.as_view(), name='DeleteEmployeeCareer'),
    path('editEmployeeCareer/<int:id>/',editEmployeeCareer.as_view(),name='editEmployeeCareer'),
    path('updateEmployeeCareer',updateEmployeeCareer.as_view(),name="updateEmployeeCareer"),




    path('employee_list/', ViewEmployeesAttendance.as_view(), name='employee_list'),
    path('get_emp_attendance_details', get_emp_attendance_details, name='get_emp_attendance_details'),

    path('add_attendance',add_attendance.as_view(),name='add_attendance'),
    path('attendance_list',attendance_List.as_view(),name='attendance_list'),
    # path('Deleteattendance',DeleteAttendance.as_view(),name='Deleteattendance'),
    path('editEmployeeAttendance/<int:id>/',editEmployeeAttendance.as_view(),name='editEmployeeAttendance'),
    path('updateEmployeeAttendance',updateEmployeeAttendance.as_view(),name="updateEmployeeAttendance"),

    

    #----------------------Employee Salary-------------------

    path('employee_list/', ViewEmployeeSalary.as_view(), name='employee_list'),
    path('get_emp_sal_details', get_emp_sal_details, name='get_emp_sal_details'),

    path('add_salary',add_salary.as_view(),name='add_salary'),
    path('salary_list',salary_list.as_view(),name='salary_list'),
    path('DeleteEmployeeSalary',DeleteEmployeeSalary.as_view(),name='DeleteEmployeeSalary'),
    path('editEmployeeSalary/<int:id>/',editEmployeeSalary.as_view(),name='editEmployeeSalary'),
    path('updateEmployeeSalary',updateEmployeeSalary.as_view(),name="updateEmployeeSalary"),



    


]