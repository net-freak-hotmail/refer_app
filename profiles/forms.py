from django import forms
from .models import *
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        user_list = kwargs.pop('user_list', None)  # Remove user_list from kwargs
        super(TaskForm, self).__init__(*args, **kwargs)
        if user_list:
            self.fields['shared_with'].queryset = User.objects.filter(id__in=[user.id for user in user_list])

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'shared_with']
