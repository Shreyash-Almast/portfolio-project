from rest_framework import serializers 
from .models import Personalinfo, Skill, Project, Education, ContactMessage

class PersonalinfoSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = Personalinfo
        fields = "__all__"

    def get_resume(self, obj):
        request = self.context.get("request")
        if obj.resume:
            return request.build_absolute_uri(obj.resume.url)
        return None

    def get_profile_pic(self, obj):
        request = self.context.get("request")
        if obj.profile_pic:
            return request.build_absolute_uri(obj.profile_pic.url)
        return None

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

