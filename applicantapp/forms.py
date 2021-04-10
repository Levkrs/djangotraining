import django.forms as forms

from applicantapp.models import Resume
from companyapp.models import Job


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', 'status', 'moder_comment', 'created_at', 'updated_at', 'views_count',]


class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class JobSearchForm(forms.Form):
    search_field = forms.CharField(required=False)
    city_field = forms.CharField(required=False)

    blank_choice = (('', '--- Пусто ---'),)
    choice_grade = forms.ChoiceField(choices=blank_choice + Job.GRADE, required=False)
    choice_category = forms.ChoiceField(choices=blank_choice + Job.CATEGORY, required=False)
    choice_employment = forms.ChoiceField(choices=blank_choice + Job.EMPLOYMENT, required=False)
    choice_work_shedule= forms.ChoiceField(choices=blank_choice + Job.WORK_SCHEDULE, required=False)
    choice_experience = forms.ChoiceField(choices=blank_choice + Job.EXPERIENCE, required=False)

    def __init__(self, *args, **kwargs):
        super(JobSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'search'
            field.help_text = ''


