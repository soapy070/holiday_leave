from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    client_squad = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    deployed_date = models.DateField()
    full_year_leave_entitlement = models.DecimalField(max_digits=5, decimal_places=2)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name


# class LeaveRequest(models.Model):
#     employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     reason = models.TextField()
#     is_sick_leave = models.BooleanField(default=False)
#     status = models.CharField(max_length=20,
#                               choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')],
#                               default='pending')

#     def __str__(self):
#         return f"{self.employee.full_name} - {self.start_date} to {self.end_date}"


# class Holiday(models.Model):
#     date = models.DateField()
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} - {self.date}"


# class CustomLoginView(LoginView):
#     template_name = 'login.html'  # Create this template
#     success_url = reverse_lazy('landing_page')


# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('landing_page')


# class RegistrationView(CreateView):
#     from .forms import RegistrationForm
#     form_class = RegistrationForm
#     template_name = 'registration.html'
#     success_url = reverse_lazy('login')

