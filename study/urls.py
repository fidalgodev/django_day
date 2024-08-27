from django.urls import path

from study.views import (
  create_new_study,
  editing_existing_study,
  list_user_studies,
  MyStudiesView,
  CreateStudyView,
  EditStudyView,
  StudiesView,
  StudyView,
)


urlpatterns = [
  path("my-studies/", list_user_studies, name="list_user_studies"),
  path("create-study/", create_new_study, name="create_new_study"),
  path("edit-study/<id>/", editing_existing_study, name="edit_existing_study"),
  path(
    "my-studies-class-based/",
    MyStudiesView.as_view(),
    name="list_user_studies_class_based",
  ),
  path(
    "create-study-class-based/",
    CreateStudyView.as_view(),
    name="create_new_study_class_based",
  ),
  path(
    "edit-study-class-based/<pk>/",
    EditStudyView.as_view(),
    name="edit_existing_study_class_based",
  ),
  # API
  path("api/all/", StudiesView.as_view(), name="api_study_list"),
  path("api/<pk>/", StudyView.as_view(), name="api_study"),
]
