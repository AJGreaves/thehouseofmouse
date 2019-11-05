from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 8,
            },
        ),
    )
    class Meta:
        fields = [
            'name',
            'email',
            'message',
        ]