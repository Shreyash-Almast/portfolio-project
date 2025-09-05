from django.contrib import admin
from .models import Personalinfo, Skill, Project, Education, ContactMessage
# Register your models here.

@admin.register(Personalinfo)
class PersonalinfoAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "linkedin", "github")
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(ContactMessage)
