from django import forms
from music.tasks import send_music_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address", widget=forms.TextInput(
        attrs={'placeholder': 'введите ваш адрес электронной почты... your_gmail@gmail.com'}))
    message = forms.URLField(label="link", widget=forms.TextInput(
        attrs={'placeholder': "Вставьте ссылку на Youtube... https://www.youtube.com/watch?v=FO2uiciLLc4"}))

    def send_email(self):
        send_music_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
