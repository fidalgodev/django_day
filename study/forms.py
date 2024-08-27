from django import forms
from study.models import Study


class StudyForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop("user")
    return super().__init__(*args, **kwargs)

  class Meta:
    model = Study

    exclude = ["creator"]

  def save(self):
    obj = super().save(commit=False)
    obj.creator = self.user
    obj.save()
    return obj
