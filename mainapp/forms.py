import django.forms as forms

from applicantapp.models import Resume
from mainapp.models import InviteRecrut, InviteHr


class IviteForm(forms.ModelForm):

    class Meta:
        model = InviteRecrut
        exclude = ['applicant','created_at','updated_at','vacansy']

class InviteFromHrForm(forms.ModelForm):
    class Meta:
        model = InviteHr
        # exclude = ['hr', 'created_at', 'updated_at', 'resume']
        fields = ['vacansy']
        # exclude=['hr','created_at', 'updated_at', 'resume']