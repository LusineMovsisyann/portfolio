from django import forms
from .models import Programmer, Project

class ProgrammerForm(forms.Forms):
    model = Programmer
    fields = "__all__"

class ProjectForm(form.Forms):
    model = Project
    fields = "__all__"
