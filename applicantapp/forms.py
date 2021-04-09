import django.forms as forms

from applicantapp.models import Resume
from companyapp.models import Job


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Resume
        # fields = '__all__'
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
    choice_grade = forms.ChoiceField(choices=Job.GRADE)
    choice_category = forms.ChoiceField(choices=Job.CATEGORY)
    choice_employment = forms.ChoiceField(choices=Job.EMPLOYMENT)
    choice_work_shedule= forms.ChoiceField(choices=Job.WORK_SCHEDULE)
    choice_experience = forms.ChoiceField(choices=Job.EXPERIENCE)
    # salary_field = forms.IntegerField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super(JobSearchForm, self).__init__(*args, **kwargs)
    #     self.fields['search_field'].widget.attrs.update({'class' : 'search_field'})

    def __init__(self, *args, **kwargs):
        super(JobSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'search'
            field.help_text = ''
        # self.fields['search_field'].widget.attrs.update({'class': 'search_field'})


