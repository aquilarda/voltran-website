from django.contrib import admin
from core.models import Member, TeamProjects, Log


class MemberAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "description"]


class ProjectsAdmin(admin.ModelAdmin):
    fields = ["project_title", "project_description"]


class LogAdmin(admin.ModelAdmin):
    fields = ["title", "description", "date"]


admin.site.register(Member, MemberAdmin)
admin.site.register(TeamProjects, ProjectsAdmin)
admin.site.register(Log, LogAdmin)
