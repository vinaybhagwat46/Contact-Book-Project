from django.shortcuts import render,HttpResponse,render,redirect
from .form import contactForm,contact_group_form,UserForm
from .models import Contact,User,Contact_Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello From Contact Page</h1>")

def home_contact(request):
    return render(request,'contact_home.html')

def insertContact(request):
    if request.method == "POST":
        f=contactForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=contactForm
        return render(request,'insertContact.html',{"abc":f})

def ViewContact(request):
    c=Contact.objects.all()
    d={"contact_list":c}
    return render(request,"viewContact.html",d)

def delete(request,id):
    d=Contact.objects.get(id=id)
    d.delete()
    return redirect('/ViewContact')

def update(request,id):
    st=Contact.objects.get(id=id)
    if request.method == 'POST':
        uc=contactForm(request.POST,instance=st)
        uc.save()
        return redirect('/')
    else:
        uc=contactForm(instance=st)
        return render(request,'insertContact.html',{'abc':uc})

def addUser(request):
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect('/')
    else:
        u=UserForm
        return render(request,'insertContact.html',{'abc':u})

def userList(request):
    ulist=User.objects.all()
    return render(request,'userList.html',{'dat':ulist})

def signIn(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        passworrd=request.POST.get('passcode')
        user=authenticate(request,username=username,password=passworrd)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'signIn.html',{'err':'Invalid Username or Password'})
    else:
        return render(request,'signIn.html')

def contactByUser(request):
    category_type_list = Contact_Group.objects.all()
    if request.method == 'POST':
        group = request.POST.get('category')
        #print('____________>>',group)
        clist1=Contact.objects.filter(category__type__icontains = group)
        #print(clist1)
        d={"contact_list":clist1,'category_list':category_type_list}
        return render(request,"viewContactByFilter.html",d)
    else:
        clist=Contact.objects.all()
        d={"contact_list":clist,'category_list':category_type_list}
        return render(request,"viewContactByFilter.html",d)


def signout(request):
    logout(request)
    return redirect('/')