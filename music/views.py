from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from music.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = "music/music.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "music/success.html"
