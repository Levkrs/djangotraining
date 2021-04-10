import django.forms as forms

from applicantapp.models import Resume
from mainapp.models import InviteRecrut, InviteHr


class IviteForm(forms.ModelForm):

    class Meta:
        model = InviteRecrut
        fields = ['resume']

class InviteFromHrForm(forms.ModelForm):
    class Meta:
        model = InviteHr
        fields = ['vacansy']