from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    model = Comment
    fields = ('comment',)

    class Meta:
        model = Comment
        fields = ('comment',)
