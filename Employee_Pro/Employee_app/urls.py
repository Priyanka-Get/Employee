from django.urls import path

from Employee_app.views import *
from . import views

urlpatterns = [
    # path('count',count,name='count'),
    path('',views.index,name='index'),
    path('profile',profile.as_view(),name='profile'),

    path('profiledetail/<int:emp_id>/',views.profiledetail,name='profiledetail'),
    path('profile_list/', profile_list.as_view(), name='profile_list'),

    
   

 

    path('E_sign_in',sign_in.as_view(),name="E_sign_in"),
    path('register_list/', ViewRegister.as_view(), name='register_list'),
    path('get_reg_details', get_reg_details, name='get_reg_details'),
    path('forgot',forgot.as_view(),name="forgot"),
    path('logout',logout_view,name="logout"),
    path('E_PasswordResetView', PasswordResetView.as_view(), name='E_PasswordResetView'),
    path('E_changePassword',changePassword.as_view(),name="E_changePassword"),
    path('E_updatePassword',updatePassword.as_view(),name="E_updatePassword"),
    #---------------employee Personal-----------

   

    path('E_employee_list/', ViewEmployees.as_view(), name='E_employee_list'),
    path('get_employee_details', get_employee_details, name='get_employee_details'),

    path('E_addemp',E_addemp.as_view(),name='E_addemp'),
    path('E_employee_list',employee_list.as_view(),name='E_employee_list'),
    path('E_DeleteEmployee', DeleteEmployee.as_view(), name='E_DeleteEmployee'),
    path('E_editEmployee/<int:id>/',editEmployee.as_view(),name='E_editEmployee'),
    path('E_updateEmployee',updateEmployee.as_view(),name="E_updateEmployee"),
    #---------------Employee Education------------------------

    path('E_employee_list/', ViewEmployeesEducation.as_view(), name='E_employee_list'),
    path('get_emp_edu_details', get_emp_edu_details, name='get_emp_edu_details'),

    path('E_addemp_education',addemp_education.as_view(),name='E_addemp_education'),
    path('E_employee_education_list',employee_education_list.as_view(),name='E_employee_education_list'),
    path('E_DeleteEmployee_education', DeleteEmployee_education.as_view(), name='E_DeleteEmployee_education'),
    path('E_editEmployeeEducation/<int:id>/',editEmployeeEducation.as_view(),name='E_editEmployeeEducation'),
    path('E_updateEmployeeEducation',updateEmployeeEducation.as_view(),name="E_updateEmployeeEducation"),
    

    #---------------Employee Career------------------------

    path('E_employee_list/', ViewEmployeesCareer.as_view(), name='E_employee_list'),
    path('get_emp_car_details', get_emp_car_details, name='get_emp_car_details'),

    path('E_addemp_career',addemp_career.as_view(),name='E_addemp_career'),
    path('E_employee_career_list',employee_career_list.as_view(),name='E_employee_career_list'),
    path('E_DeleteEmployeeCareer', DeleteEmployeeCareer.as_view(), name='E_DeleteEmployeeCareer'),
    path('E_editEmployeeCareer/<int:id>/',editEmployeeCareer.as_view(),name='E_editEmployeeCareer'),
    path('E_updateEmployeeCareer',updateEmployeeCareer.as_view(),name="E_updateEmployeeCareer"),




    path('E_employee_list/', ViewEmployeesAttendance.as_view(), name='E_employee_list'),
    path('get_emp_attendance_details', get_emp_attendance_details, name='get_emp_attendance_details'),

    path('E_add_attendance',add_attendance.as_view(),name='E_add_attendance'),
    path('E_attendance_list',attendance_List.as_view(),name='E_attendance_list'),
    # path('Deleteattendance',DeleteAttendance.as_view(),name='Deleteattendance'),
    path('E_editEmployeeAttendance/<int:id>/',editEmployeeAttendance.as_view(),name='E_editEmployeeAttendance'),
    path('E_updateEmployeeAttendance',updateEmployeeAttendance.as_view(),name="E_updateEmployeeAttendance"),

    

    #----------------------Employee Salary-------------------

    path('E_employee_list/', ViewEmployeeSalary.as_view(), name='E_employee_list'),
    path('get_emp_sal_details', get_emp_sal_details, name='get_emp_sal_details'),

    path('E_add_salary',add_salary.as_view(),name='E_add_salary'),
    path('E_salary_list',salary_list.as_view(),name='E_salary_list'),
    path('E_DeleteEmployeeSalary',DeleteEmployeeSalary.as_view(),name='E_DeleteEmployeeSalary'),
    path('E_editEmployeeSalary/<int:id>/',editEmployeeSalary.as_view(),name='E_editEmployeeSalary'),
    path('E_updateEmployeeSalary',updateEmployeeSalary.as_view(),name="E_updateEmployeeSalary"),



    path('E_comp_list/', ViewCompany.as_view(), name='E_comp_list'),
    path('get_company_details', get_company_details, name='get_company_details'),
    path('E_addcomp',addcomp.as_view(),name='E_addcomp'),
    path('E_comp_list',comp_list.as_view(),name='E_comp_list'),
    path('E_DeleteCompany',DeleteCompany.as_view(),name='E_DeleteCompanyy'),
    path('E_editCompany/<int:id>/',editCompany.as_view(),name='E_editCompany'),
    path('E_updateCompany',updateCompany.as_view(),name="E_updateCompany"),



]