from django import forms
from django.utils.translation import ugettext_lazy as _

from post.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control', "placeholder": _('Имя')}),
            "subject": forms.TextInput(attrs={"class": 'form-control', "placeholder": _('Тема')}),
            "messages": forms.Textarea(attrs={"class": 'form-control', "placeholder": _('Сообщения'), "rows": 5}),
        }