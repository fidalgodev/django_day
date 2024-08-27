from django.urls import path

from study.views import create_new_study, editing_existing_study


urlpatterns = [
  path("create-study/", create_new_study, name="create_new_study"),
  path("edit-study/<id>/", editing_existing_study, name="edit_existing_study"),
]
