import django.forms as forms

from applicantapp.models import Resume


class ResumeSearchForm(forms.Form):
    blank_choice = (('', '--- Пусто ---'),)
    search_field = forms.CharField(required=False)
    city_field = forms.CharField(required=False)
    education_type = forms.ChoiceField(choices=blank_choice + Resume.EDUCATION_CHOICES)
    employment = forms.ChoiceField(choices=blank_choice + Resume.EMPLOYMENT_CHOICES)
    work_schedule = forms.ChoiceField(choices=blank_choice + Resume.WORK_SCHEDULE_CHOICES)



    def __init__(self, *args, **kwargs):
        super(ResumeSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'search'
            field.help_text = ''