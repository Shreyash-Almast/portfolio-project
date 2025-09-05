from rest_framework import generics
from .models import Personalinfo, Skill, Project, Education, ContactMessage
from .serializers import PersonalinfoSerializer, SkillSerializer, ProjectSerializer, EducationSerializer, ContactMessageSerializer

class PersonalinfoList(generics.ListAPIView):
    queryset = Personalinfo.objects.all()
    serializer_class = PersonalinfoSerializer

class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EducationList(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ContactMessageCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
