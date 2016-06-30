from django import forms
from projects.models import Project, Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = '__all__'
