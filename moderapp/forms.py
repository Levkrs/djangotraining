import django.forms as forms

from applicantapp.models import Resume

class ResumeForChecked(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
from companyapp.models import Job, Company


class ResumeModerateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name not in ['status', 'moder_comment']:
                field.widget.attrs['readonly'] = True


class JobModerateForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name not in ['status', 'moder_comment']:
                field.widget.attrs['readonly'] = True


class CompanyModerateForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name not in ['status', 'moder_comment']:
                field.widget.attrs['readonly'] = True