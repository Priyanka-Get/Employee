from django.db import models

# Create your models here.
class EmployeePersonal(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phno = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    adhar_no = models.CharField(max_length=100, null=False, blank=False)
    pan_no = models.CharField(max_length=100,null=False,blank=False)

class EmployeeEucation(models.Model):
    empedu_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    percentage= models.CharField(max_length=100, null=True, blank=True)
    pass_out = models.DateField(null=False, blank=False)

class EmployeeCareer(models.Model):
    empcar_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)    
  

 
class Attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])



class Salary(models.Model):
    sal_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)

    base_salary = models.DecimalField(max_digits=50, decimal_places=2)
    hra = models.DecimalField(max_digits=50, decimal_places=2)
    allowance = models.DecimalField(max_digits=50, decimal_places=2)
    bonus = models.DecimalField(max_digits=50, decimal_places=2)
    ctc = models.DecimalField(max_digits=50, decimal_places=2)

 
class Register(models.Model):
  
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=128)
    role=models.CharField(max_length=50)   

class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=100, null=True, blank=True)
    cEmail = models.CharField(max_length=100, null=False, blank=False)
    cUrl = models.CharField(max_length=50)
    cAddress = models.CharField(max_length=100, null=False, blank=False)
    cPhno = models.CharField(max_length=100, null=False, blank=False)



class Profiledetail(models.Model):
    pro_id = models.AutoField(primary_key=True)
    
    education = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    career = models.ForeignKey(EmployeeEucation, on_delete=models.CASCADE)
    attendance = models.ForeignKey(EmployeeCareer, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    
