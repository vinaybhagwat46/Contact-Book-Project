import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','contact_simple.settings')

import django
django.setup()

#Fake pop script
import random
from first_contact.models import *
from faker import Faker

fakegen = Faker()
category=['Family','Friends','Business','General','Factroy']
User_list  = ['tester', 'vinay','Ajay']

def add_category():
    t = Contact_Group.objects.get_or_create(type=random.choice(category))[0]
    t.save()
    return t

def add_user():
    a = User.objects.get_or_create(type=random.choice(User_list))[0]
    a.save()
    return a

def populate(N=5):
    for entry in range(N):

        #Categorty for entry
        top = add_category()
        top12 = add_user()

        #Create the fake data
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_Contact = fakegen.msisdn()
        fake_email = fakegen.ascii_free_email()
        fake_address =  fakegen.street_address()

        # Create contact entry

        contact_pg = Contact.objects.get_or_create(first_name=fake_firstName,last_name=fake_lastName,contact=fake_Contact,email=fake_email,address=fake_address,category=top,user='vinay')

if __name__ == '__main__':
    print('POpulating script!')
    populate(20)
    print('populating complete!')
