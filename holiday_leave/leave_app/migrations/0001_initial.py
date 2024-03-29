# Generated by Django 4.2.4 on 2023-09-01 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('client_squad', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('deployed_date', models.DateField()),
                ('full_year_leave_entitlement', models.DecimalField(decimal_places=2, max_digits=5)),
                ('manager_emp_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('is_sick_leave', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')], default='pending', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_app.employee')),
            ],
        ),
    ]
