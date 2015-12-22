from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from .forms import SignUpForm,Contact
def home(request):
    print request
    if request.method=="POST":
        print request.method

    form=SignUpForm(request.POST or None)
    if form.is_valid():
        me=form.save(commit=True)
        print me

    title="Welcome to my website %s " %(request.user)
    context={
      "tem":title,
      "form":form
    }
    return render(request,"home.html",context)
def contact(request):
    form=Contact(request.POST or None)
    contact="Contact Us"
    if form.is_valid():
        #.........................1 way to read form data
        full_name=form.cleaned_data.get("full_name")
        email=form.cleaned_data.get("email")
        message=form.cleaned_data.get("message") 
        print full_name,email,message
        #............................... another way to read form data
        #for i in form.cleaned_data:
            #print i
            #print form.cleaned_data.get(i)
        #for i,j in form.cleaned_data.items():
            #print i,j
        full_name=form.cleaned_data.get("full_name")
        email=form.cleaned_data.get("email")
        message=form.cleaned_data.get("message")
        Subject="contact form test"
        from_email="ikfbouba@gmail.com"
        to_email="ikfbouba@gmail.com"
        send_mail(Subject,message, from_email,[to_email], fail_silently=True)

    context={
    "form":form,
    "contact":contact,
    }
    return render(request,"form.html",context)
def example(request):
    return render(request,"examplefluid.html")
def about(request):
    return render(request,"about.html")
