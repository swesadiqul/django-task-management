from django import forms
from tasks.models import *


#create forms here
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'status']


