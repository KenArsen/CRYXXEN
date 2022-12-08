from django.urls import path
from music.views import FeedbackFormView, SuccessView

app_name = "music"

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="music"),
    path("success/", SuccessView.as_view(), name="success"),
]
