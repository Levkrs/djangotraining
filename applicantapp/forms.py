import django.forms as forms

from applicantapp.models import Resume


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

