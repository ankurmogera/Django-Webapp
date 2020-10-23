from django.shortcuts import render, redirect, get_object_or_404
from contacts.forms import contactRecordForms
from contacts.models import contactRecords

# Create your views here.
def dashboard(request):
    print(request)
    data = contactRecords.objects.filter(is_active = True)
    return render(request, 'dashboard.html', {'data' : data})


def add(request):                                   # view to add contacts

    if request.method == 'POST':
        form = contactRecordForms(request.POST) # populates the form with user data

        if form.is_valid():
            phone_number = request.POST.get('phone_number')     # retrieves the phone number from user data
            result = contactRecords.objects.filter(phone_number = phone_number)     # filters all records with user phone_number
            print(result)                                                                            # and puts in result
            print(len(result))
            if len(result) > 1:                                # if result value is more than 1
                contactBookObj = get_object_or_404(contactRecords, pk=result[0].id)             # gets the first record in the result
                print(contactBookObj)
                contactBookObj.is_active = True                                                 # makes the is_active field to True
                contactBookObj.save()
            else:                           # else save the form with user data
                form.save()

            return redirect('add')

    form = contactRecordForms()                 # if request method is get, shows a blank form
    return render(request, 'add.html', {'form':form, 'title': 'Add New Contact', 'button': 'Add'})

def edit(request, id):

    # Get the record by 'id' from the table in database
    contactBookObj = get_object_or_404(contactRecords, pk=id)

    if request.method == 'POST':
        # Populate the form with the user data
        form = contactRecordForms(request.POST, instance=contactBookObj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = contactRecordForms()

    # Populate the form with the retrieved record
    form = contactRecordForms(instance=contactBookObj)

    # Return the html page with the populated page
    return render(request, 'add.html', {'form':form, 'title': 'Edit Contact', 'button': 'Edit'})

def delete(request, id):

    # Get the record by 'id' from the table in database
    contactBookObj = get_object_or_404(contactRecords, pk=id)
    # Make the is_active field 'false' in the object
    contactBookObj.is_active = False
    # Save the object by save() method
    contactBookObj.save()

    return redirect('dashboard')


