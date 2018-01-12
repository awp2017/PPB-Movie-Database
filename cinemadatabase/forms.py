from django import forms
from django.utils import timezone
from taskmanager.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(input_formats=["%m/%d/%Y %I:%M %p"])

    class Meta:
        model = Task
        fields = (
            'title', 'description', 'category', 'deadline', 
            'group', 'responsible'
        )

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        if data and data < timezone.now():
            raise forms.ValidationError("Deadline must not be in the past!")
        return data
        

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
