from django import forms


class EmailForm(forms.Form):

    email = forms.EmailField(max_length=128, required=True, label=False)


    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'rounded-0'
        self.fields['email'].widget.attrs['placeholder'] = 'Insert Email Here'
        self.fields['email'].widget.attrs['id'] = 'mailchimp'
       




    