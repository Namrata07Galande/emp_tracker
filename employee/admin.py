from django.contrib import admin

# Register your models here.
from employee.models import employee,emp_leave,holiday
admin.site.register(employee)
admin.site.register(emp_leave)
admin.site.register(holiday)