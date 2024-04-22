from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'grade', 'good', 'bad', 'ideas']
        # widgets = {
        #     'good': forms.Textarea(attrs={'rows': 3}),
        #     'bad': forms.Textarea(attrs={'rows': 3}),
        #     'ideas': forms.Textarea(attrs={'rows': 3}),
        # }