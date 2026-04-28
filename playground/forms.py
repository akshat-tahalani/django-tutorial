from django import forms
from .models import Review

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    subject  = forms.CharField(max_length=100)
    message = forms.CharField(widget =forms.Textarea)
    option = forms.CheckboxInput()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3 :
            raise forms.ValidationError("naam 3 badha de")
        return name

    def clean_message(self):
        message  = self.cleaned_data.get('message')
        if 'spam' in message.lower():
            raise forms.ValidationError("spam detect")
        return message



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']
    
