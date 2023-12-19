from django import forms
from .models import Profile
#from lessons.models import Student


class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
            'country' : 'Country'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False



"""
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 
                    'last_name',
                    'dob',
                    'userAccount'
                    )

    def __init__(self, *args, **kwargs):
        """
"""
Add placeholders and classes, remove auto-generated
labels and set autofocus on first field
"""
"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Frst Name', 
            'last_name': 'Last Name',
            'userAccount',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
"""