from django import forms
from game.models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']