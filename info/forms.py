from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=200)
    contact = forms.IntegerField(label='Contact number')
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Clean data
    def clean_data(self):
        data = self.cleaned_data['name', 'message', 'email', 'contact']
        return data

    class Meta:
        fields = ('name', 'message', 'email', 'contact')









