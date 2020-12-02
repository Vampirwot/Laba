from django import forms


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=20, min_length=1)
    last_name = forms.CharField(max_length=20, min_length=1)
    phone = forms.RegexField(regex='^((8)+([0-9]){10})$')
    message = forms.CharField(widget=forms.Textarea, max_length=100, min_length=1)
    file = forms.FileField(max_length=30)
