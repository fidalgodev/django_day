from django.shortcuts import render, redirect
from study.forms import StudyForm
from study.models import Study
from django.urls import reverse


def create_new_study(request):
  if request.method == "GET":
    form = StudyForm(user=request.user)

  else:
    form = StudyForm(request.POST, user=request.user)

    if form.is_valid():
      form.save()

      return redirect(reverse("home"))

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

      return redirect(reverse("home"))

  return render(
    request,
    "create_study.html",
    {"form": form},
  )
