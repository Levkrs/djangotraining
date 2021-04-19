import django.forms as forms

from applicantapp.models import Resume
from companyapp.models import Job


class ResumeCreateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', 'moder_comment', 'views_count', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in ['status']:
                field.widget = forms.HiddenInput()


class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in ['status', 'moder_comment', 'views_count']:
                field.widget.attrs['readonly'] = True


class JobSearchForm(forms.Form):
    search_field = forms.CharField(required=False, help_text='Поиск..')
    city_field = forms.CharField(required=False, help_text='Город')

    blank_choice = (('', '--- Пусто ---'),)
    choice_grade = forms.ChoiceField(choices=blank_choice + Job.GRADE, required=False,
                                     help_text='Степень')
    choice_category = forms.ChoiceField(choices=blank_choice + Job.CATEGORY, required=False,
                                        help_text='Направление')
    choice_employment = forms.ChoiceField(choices=blank_choice + Job.EMPLOYMENT, required=False,
                                          help_text='Образование')
    choice_work_shedule= forms.ChoiceField(choices=blank_choice + Job.WORK_SCHEDULE, required=False,
                                           help_text='График работы')
    choice_experience = forms.ChoiceField(choices=blank_choice + Job.EXPERIENCE, required=False,
                                          help_text='Опыт работы')

    def __init__(self, *args, **kwargs):
        super(JobSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'search'
            field.help_text = ''
