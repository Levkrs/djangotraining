import django.forms as forms

from applicantapp.models import Resume


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Resume
        # fields = '__all__'
        exclude = ['user_id', 'is_cheked', 'moder_comment']
