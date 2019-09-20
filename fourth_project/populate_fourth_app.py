import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourth_project.settings')

import django
django.setup()

# Fake Population script
import random
from fourth_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):

    for entry in range(n):

        #create fake data
        name = fakegen.name()
        fake_name = list(name.split())
        a= fake_name.pop(0)
        b= fake_name.pop(-1)
        e_domain= fakegen.free_email_domain()
        f_email = str.lower(a+b+"@"+e_domain)

        #load the fake entry into model

        user_fake= User.objects.get_or_create(full_name=name,first_name=a,last_name=b,email=f_email)[0]


if __name__ == "__main__":
    print("populating script!")
    populate(10)
    print("populating complete!")


    



        
