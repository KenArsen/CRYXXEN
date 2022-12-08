from django import forms
from music.tasks import send_music_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.URLField(label="link")

    def send_email(self):
        send_music_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
