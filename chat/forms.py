from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your message here...',
        'rows': 2,
        'class': 'input-box',
    }))
