# Generated by Django 4.2.7 on 2024-01-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePersonal',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('adhar_no', models.CharField(max_length=100)),
                ('pan_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('sal_id', models.AutoField(primary_key=True, serialize=False)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=50)),
                ('hra', models.DecimalField(decimal_places=2, max_digits=50)),
                ('allowance', models.DecimalField(decimal_places=2, max_digits=50)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=50)),
                ('ctc', models.DecimalField(decimal_places=2, max_digits=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.employeepersonal')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEucation',
            fields=[
                ('empedu_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(blank=True, max_length=100, null=True)),
                ('university', models.CharField(blank=True, max_length=100, null=True)),
                ('percentage', models.CharField(blank=True, max_length=100, null=True)),
                ('pass_out', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.employeepersonal')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCareer',
            fields=[
                ('empcar_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.employeepersonal')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.employeepersonal')),
            ],
        ),
    ]