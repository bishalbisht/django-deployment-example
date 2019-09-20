from django.shortcuts import render
from django.http import HttpResponse
from fourth_app.models import User
from fourth_app.forms import contact_form

# Create your views here.

def index(request):
    contact= contact_form()

 # Create a form instance from POST data.
    if request.method == 'POST':
         contact= contact_form(request.POST)

         if contact.is_valid():
            contact.save(commit=True)
        
         else:
            print('error form invalid')

    return render (request, 'index.html', {'index_form': contact})

# Create a form to edit an existing User, but use
# POST data to populate the form.
    
    cm=User.objects.get(pk=1)
    contact=contact_form(request.POST,instance=cm)
    contact.save() 


def user(request):
    user_list = User.objects.order_by('full_name')
    user_dict = { 'user_records': user_list}
    return render(request, 'user.html', context= user_dict)

    
    







    