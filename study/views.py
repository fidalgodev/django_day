from django.shortcuts import render, redirect
from study.forms import StudyForm
from study.models import Study
from study.serializers import StudySerializer
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from rest_framework import generics as rest_views


def create_new_study(request):
  if request.method == "GET":
    form = StudyForm(user=request.user)

  else:
    form = StudyForm(request.POST, user=request.user)

    if form.is_valid():
      form.save()

      return redirect(reverse_lazy("list_user_studies"))

  return render(
    request,
    "create_study.html",
    {"form": form},
  )


def editing_existing_study(request, id):
  study = Study.objects.get(id=id)

  if request.method == "GET":
    form = StudyForm(instance=study, user=request.user)

  else:
    form = StudyForm(request.POST, instance=study, user=request.user)

    if form.is_valid():
      form.save()

      return redirect(reverse_lazy("list_user_studies"))

  return render(
    request,
    "create_study.html",
    {"form": form},
  )


def list_user_studies(request):
  studies = Study.objects.filter(creator=request.user)

  return render(
    request,
    "list_studies.html",
    {"studies": studies},
  )


class MyStudiesView(ListView):
  template_name = "list_studies.html"
  context_object_name = "studies"

  def get_queryset(self):
    return Study.objects.filter(creator=self.request.user)


class CreateStudyView(CreateView):
  model = Study
  template_name = "create_study.html"
  form_class = StudyForm
  success_url = reverse_lazy("list_user_studies_class_based")

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs["user"] = self.request.user

    return kwargs


class EditStudyView(UpdateView):
  template_name = "create_study.html"
  form_class = StudyForm
  success_url = reverse_lazy("list_user_studies_class_based")

  # Filter the queryset to only show the studies created by the current user are possible to edit
  def get_queryset(self):
    return Study.objects.filter(creator=self.request.user)

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs["user"] = self.request.user

    return kwargs


class StudiesView(rest_views.ListCreateAPIView):
  serializer_class = StudySerializer

  def get_queryset(self):
    return Study.objects.filter(creator=self.request.user)
