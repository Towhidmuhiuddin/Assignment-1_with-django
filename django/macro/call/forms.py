from .models import School, Subject, Teacher
from django import forms

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'        