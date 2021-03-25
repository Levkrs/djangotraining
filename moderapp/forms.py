import django.forms as forms

from applicantapp.models import Resume

class ResumeForChecked(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
