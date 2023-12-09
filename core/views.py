from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from core.models import Member, TeamProjects, Log


class IndexView(View):
    def get(self, request):
        members = Member.objects.all()
        template_params = {"members": members}

        return render(request, "index.html", template_params)


class MembersView(APIView):
    def get(self, request):
        members = Member.objects.all()
        serialized_members = [m.serialize() for m in members]
        return JsonResponse(serialized_members, safe=False)


class ProjectsView(APIView):
    def get(self, request):
        projects = TeamProjects.objects.all()
        serialized_projects = [p.serialize() for p in projects]
        return JsonResponse(serialized_projects, safe=False)


class LogsView(APIView):
    def get(self, request):
        logs = Log.objects.all()
        serialized_logs = [l.serialize() for l in logs]
        return JsonResponse(serialized_logs, safe=False)
