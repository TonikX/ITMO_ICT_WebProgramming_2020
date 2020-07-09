from django import forms
from .models import Patient, Doctor, App_times, Schedule, Medical_Record, Appointment
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(10, 18)]

#        time = forms.ModelChoiceField(
#            queryset=Schedule.objects.values_list("work_time", flat=True).distinct(),
#            empty_label=None
#        )

class TimeForm(forms.ModelForm):

        class Meta:
            model = Appointment
            fields = ('doc', 'patient', 'time', 'date', 'paid')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['time'].queryset = Schedule.objects.none()

            if 'doc' in self.data:
                try:
                    doc_id = int(self.data.get('doc'))
                    self.fields['time'].queryset = Schedule.objects.filter(doc_id=doc_id).order_by('work_time')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['time'].queryset = self.instance.shedule.doc_set.order_by('work_time')

#class AppForm(forms.ModelForm):

#    class Meta:
#        model = Appointment
#        fields = ('doc', 'patient', 'date', 'paid')
#        widgets = {'time': forms.Select(choices=HOUR_CHOICES)}
