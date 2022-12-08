from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import School, Subject, Teacher
from .forms import SchoolForm, SubjectForm, TeacherForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "call/home.html"


class SchoolCreate(CreateView):
    model = School
    form_class = SchoolForm
    template_name = "call/create.html"

class SchoolView(ListView):
    model = School
    template_name = "call/schoollist.html"

class SubjectCreate(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "call/create.html"

class SubjectView(ListView):
    model = Subject
    template_name = "call/subjectlist.html"

class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name= "call/create.html"

class TeacherView(ListView):
    model = Teacher
    template_name = "call/teacherlist.html"        