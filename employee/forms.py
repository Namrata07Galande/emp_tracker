from django.forms import ModelForm
from employee.models import employee,emp_leave,holiday
class empform(ModelForm):
    class Meta:
        model = employee

        fields = '__all__'

class leaveform(ModelForm):
    class Meta:
        model = emp_leave

        fields = '__all__'


class holidayform(ModelForm):
    class Meta:
        model = holiday

        fields = '__all__'
