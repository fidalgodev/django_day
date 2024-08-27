from django.shortcuts import render, redirect
from study.forms import StudyForm
from study.models import Study
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView


def create_new_study(request):
  if request.method == "GET":
    form = StudyForm(user=request.user)

  else:
    form = StudyForm(request.POST, user=request.user)

    if form.is_valid():
      form.save()

      return redirect(reverse("list_user_studies"))

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

      return redirect(reverse("list_user_studies"))

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

  def get_form(self):
    return StudyForm(user=self.request.user)


class EditStudyView(UpdateView):
  model = Study
  template_name = "create_study.html"

  def get_queryset(self):
    return Study.objects.filter(creator=self.request.user)

  def get_form(self):
    return StudyForm(user=self.request.user)
