from django import forms
from .models import BookSend

class BookSendForm(forms.ModelForm):
    class Meta:
        model = BookSend
        fields = ['ref_no', 'date', 'sender', 'receiver', 'subject', 'action', 'remark']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }