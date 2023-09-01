from django.shortcuts import render, redirect
from .models import LeaveRequest, Holiday
from .forms import RegistrationForm  # Adjust imports based on the provided code
import holidays
from datetime import datetime


def landing_page(request):
    return render(request, 'landing_page.html')


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')  # Redirect to a list view of employees
    else:
        form = EmployeeForm()

    return render(request, 'create_employee.html', {'form': form})


def create_manager(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager-list')  # Redirect to a list view of employees
    else:
        form = EmployeeForm()

    return render(request, 'create_employee.html', {'form': form})

def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employee
            leave_request.save()
            return redirect('leave_requests')  # Redirect to a list of leave requests
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request.html', {'form': form})


def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'holiday_list.html', {'holidays': holidays})


def public_holidays(request):
    current_year = datetime.now().year

    uk_holidays = sorted(holidays.UK(years=current_year).items(), key=lambda x: x[0])
    eng_holidays = sorted(holidays.UK(years=current_year, subdiv="ENG").items(), key=lambda x: x[0])
    sct_holidays = sorted(holidays.UK(years=current_year, subdiv="SCT").items(), key=lambda x: x[0])
    wls_holidays = sorted(holidays.UK(years=current_year, subdiv="WLS").items(), key=lambda x: x[0])
    nir_holidays = sorted(holidays.UK(years=current_year, subdiv="NIR").items(), key=lambda x: x[0])
    ca_holidays = sorted(holidays.CA(years=current_year).items(), key=lambda x: x[0])
    au_holidays = sorted(holidays.AU(years=current_year).items(), key=lambda x: x[0])
    us_holidays = sorted(holidays.US(years=current_year).items(), key=lambda x: x[0])

    context = {
        'uk_holidays': uk_holidays,
        'eng_holidays': eng_holidays,
        'sct_holidays': sct_holidays,
        'wls_holidays': wls_holidays,
        'nir_holidays': nir_holidays,
        'ca_holidays': ca_holidays,
        'au_holidays': au_holidays,
        'us_holidays': us_holidays,
    }

    return render(request, 'holiday_app/holiday_list.html', context)
