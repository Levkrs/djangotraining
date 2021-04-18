import django.forms as forms

from applicantapp.models import Resume, Education
from companyapp.models import Company


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user', 'created_at', 'updated_at', 'views_count']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in ['status', 'moder_comment'] :
                field.widget.attrs['readonly'] = True


class ResumeSearchForm(forms.Form):
    blank_choice = (('', '--- Пусто ---'),)
    search_field = forms.CharField(required=False)
    city_field = forms.CharField(required=False)
    education_type = forms.ChoiceField(choices=blank_choice + Education.EDUCATION_CHOICES,
                                       required=False)
    employment = forms.ChoiceField(choices=blank_choice + Resume.EMPLOYMENT_CHOICES,
                                   required=False)
    work_schedule = forms.ChoiceField(choices=blank_choice + Resume.WORK_SCHEDULE_CHOICES,
                                      required=False)



    def __init__(self, *args, **kwargs):
        super(ResumeSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'search'
            field.help_text = ''