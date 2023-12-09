from django.db import models


class Member(models.Model):
    first_name = models.CharField("İsim", max_length=18)
    last_name = models.CharField("Soy isim", max_length=18)
    description = models.TextField("Açıklama", blank=True)

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"

    def __str__(self):
        return self.first_name


class TeamProjects(models.Model):
    project_title = models.CharField("Proje Başlığı", max_length=70)
    project_description = models.TextField("Proje Açıklaması")

    class Meta:
        verbose_name = "team project"
        verbose_name_plural = "team projects"

    def __str__(self):
        return self.project_title


class Log(models.Model):
    title = models.CharField("Başlık", max_length=60)
    description = models.TextField("Açıklama")
    date = models.DateTimeField("Tarih")

    class Meta:
        verbose_name = "log"
        verbose_name_plural = "logs"

    def __str__(self):
        return self.title
