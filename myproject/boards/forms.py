from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Qué tienes en tu mente...?'}
        ),
        max_length=4000,
        help_text = 'La extensión máxima del texto es 4000'
        )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

