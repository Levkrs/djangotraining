import django.forms as forms

from applicantapp.models import Resume
from mainapp.models import FullInvite


class FullInviteForm(forms.ModelForm):
    class Meta:
        model= FullInvite
        # fields = '__all__'
        fields = ['vacansy']

class FullInviteFormUser(forms.ModelForm):
    class Meta:
        model= FullInvite
        # fields = '__all__'
        fields = ['recrut_resume']