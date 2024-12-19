from django.forms import ModelForm

from .models import TodoTask


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTask
        fields = "__all__"
        exclude = ["owner"]
