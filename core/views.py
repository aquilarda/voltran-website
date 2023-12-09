from django.shortcuts import render
from django.views import View
from core.models import Member, TeamProjects, Log


class IndexView(View):
    def get(self, request):
        members = Member.objects.all()
        context = {"members": members}
        return render(request, "index.html", context)
