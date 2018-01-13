from django import forms
from django.utils import timezone
from cinemadatabase.models import Discussion, Comment


class DiscussionForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'cols': 22, 'rows': 8}))
    
    
class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'cols': 22, 'rows': 8}))

# class TaskForm(forms.ModelForm):
#     deadline = forms.DateTimeField(input_formats=["%m/%d/%Y %I:%M %p"])

#     class Meta:
#         model = Task
#         fields = (
#             'title', 'description', 'category', 'deadline', 
#             'group', 'responsible'
#         )

#     def clean_deadline(self):
#         data = self.cleaned_data['deadline']
#         if data and data < timezone.now():
#             raise forms.ValidationError("Deadline must not be in the past!")
#         return data

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
