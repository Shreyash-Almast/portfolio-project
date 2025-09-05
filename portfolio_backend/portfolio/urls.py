from django.urls import path
from .views import PersonalinfoList, SkillList, ProjectList, EducationList, ContactMessageCreate

urlpatterns = [
    path('personal-info/', PersonalinfoList.as_view(), name='personal-info'),
    path('skills/', SkillList.as_view(), name='skills'),
    path('projects/', ProjectList.as_view(), name='projects'),
    path('education/', EducationList.as_view(), name='education'),
    path('contact/', ContactMessageCreate.as_view(), name='contact'),
]
