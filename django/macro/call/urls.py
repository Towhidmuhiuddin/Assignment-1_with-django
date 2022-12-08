from django.urls import path, include
from call.views import HomeView, SchoolCreate,  SchoolView, SubjectView, SubjectCreate , TeacherCreate,TeacherView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # New views below
    path('create-school/', SchoolCreate.as_view(), name="schoolcreate"),
    path('list-school/', SchoolView.as_view(), name="schoollist"),
    path('create-subject/', SubjectCreate.as_view(), name="subjectcreate"),
    path('list-subject/', SubjectView.as_view(), name="subjectlist"),
    path('create-teacher/', TeacherCreate.as_view(), name="teachercreate"),
    path('list-teacher/', TeacherView.as_view(), name="teacherlist"),
]