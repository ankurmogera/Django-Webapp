from django import forms                    # forms is the module in django
from contacts.models import contactRecords  # contactRecords is the class(model) created in models.py

class contactRecordForms(forms.ModelForm):  # new class contactRecordForms created and inherited from ModelForm class

    def __init__(self, *args, **kwargs):
        super(contactRecordForms,self).__init__(*args, **kwargs)
        self.fields['dob'].widget = forms.DateInput(attrs = { 'type' : 'date'})
        self.fields['dob'].label = 'Date of Birth'
        self.fields['email'].widget = forms.EmailInput(attrs={ 'type' : 'email'})

    class Meta():
        model = contactRecords
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'dob')

