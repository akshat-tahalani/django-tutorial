from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    subject  = forms.CharField(max_length=100)
    message = forms.CharField(widget =forms.Textarea)
    option = forms.CheckboxInput()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3 :
            raise forms
