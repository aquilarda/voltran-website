from django.contrib import admin
from django.urls import path
from core.views import IndexView, MembersView, ProjectsView, LogsView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="main-page"),
    path("api/members/", MembersView.as_view(), name="GET members"),
    path("api/projects/", ProjectsView.as_view(), name="GET projects"),
    path("api/logs/", LogsView.as_view(), name="GET logs"),
]
