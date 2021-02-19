from django.shortcuts import render
from .models import New, Event,Department,HOD
from MainPage.models import mci
from django.template import loader
from django.contrib.auth.models import User
from django.core.mail import send_mail
from MainPage.forms import SubscriberForm


# Create your views here.
def index(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'news': New.objects.all(),
        'events': Event.objects.all()
    }
    return render(request, 'college/index.html',context)


def news(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'news': New.objects.all(),
        'events': Event.objects.all()

    }
    return render(request, 'college/news.html', context)

# facilities

def facility(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request, 'college/facilities/facilities.html',{'form':form})
# facilities

def centralab(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        
    return render(request,'college/facilities/centralab.html',{'form':form})

def library(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        
    return render(request,'college/facilities/library.html',{'form':form})

def infrastructure(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/facilities/infrastructure.html',{'form':form}) 

def internetsection(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        
    return render(request,'college/facilities/internetsection.html',{'form':form})  

def seminar(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        
    return render(request,'college/facilities/seminar.html',{'form':form})  

def canteen(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/facilities/canteen.html',{'form':form})                  

def hostel(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        
    return render(request,'college/facilities/hostel.html',{'form':form})   

def anti(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/facilities/antiragging.html',{'form':form})  

def transport(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/facilities/transport.html',{'form':form})   

# mci clause 

def mcic(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'mci': mci.objects.all()

    }
    return render(request, 'college/mci.html',context)



# Departments

def physiology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'physio': Department.objects.filter(Name="1")

    }
    return render(request,'college/department/physiology.html', context)

def anatomy(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Anatomy': Department.objects.filter(Name="2")
    }
    return render(request,'college/department/anatomy.html', context)

def cm(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Community': Department.objects.filter(Name="3"),
    }
    return render(request,'college/department/cm.html', context)

def tb(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Tb': Department.objects.filter(Name="4"),
    }
    return render(request,'college/department/tb.html', context)

def Paediatrics(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Paediatrics': Department.objects.filter(Name="5"),
    }
    return render(request,'college/department/Paediatrics.html', context)

def Orthopaedics(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Orthopaedics': Department.objects.filter(Name="6"),
    }
    return render(request,'college/department/Orthopaedics.html', context)

def Opthalmology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Opthalmology': Department.objects.filter(Name="7"),
    }
    return render(request,'college/department/Opthalmology.html', context)

def Psychiatry(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Psychiatry': Department.objects.filter(Name="8"),
    }
    return render(request,'college/department/Psychiatry.html', context)

def Obstetrics(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Obstetrics': Department.objects.filter(Name="9"),

    }
    return render(request,'college/department/Obstetrics.html', context)

def gs(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'General': Department.objects.filter(Name="10"),
    }
    return render(request,'college/department/gs.html', context)

def fm(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Forensic': Department.objects.filter(Name="11"),
    }
    return render(request,'college/department/fm.html', context)

def ent(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'ENT': Department.objects.filter(Name="12"),
    }
    return render(request,'college/department/ent.html', context)

def Dermatology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Dermatology': Department.objects.filter(Name="13"),
    } 
    return render(request,'college/department/Dermatology.html', context)

def Dentistry(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
             'Dentistry': Department.objects.filter(Name="14"),
    }
    return render(request,'college/department/Dentistry.html', context)


def Anaesthesiology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Anaesthesiology': Department.objects.filter(Name="15"),

    }
    return render(request,'college/department/Anaesthesiology.html', context)


def Pharmacology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
                'form':form,
                'Pharmacology': Department.objects.filter(Name="16"),
    }
    return render(request,'college/department/Pharmacology.html', context)

def bc(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Bio': Department.objects.filter(Name="17"),
    }
    return render(request,'college/department/bc.html', context)

def Pathology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
             'Pathology': Department.objects.filter(Name="18"),
    }
    return render(request,'college/department/Pathology.html', context)

def mb(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Micro': Department.objects.filter(Name="19"),
    }
    return render(request,'college/department/mb.html', context)

def rd(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Radio': Department.objects.filter(Name="20"),
    }
    return render(request,'college/department/rd.html', context)

def gm(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
            'form':form,
            'Generalm': Department.objects.filter(Name="21"),
    }
    return render(request,'college/department/gm.html', context)

    #ourgroup
def ourgroup(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/ourgroup/ourgp.html',{'form':form}) 
    
    #research
def cme(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/research/cme.html',{'form':form}) 

def paper(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
       
    return render(request,'college/research/paper.html',{'form':form})

def researchproj(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form

    }
    return render(request,'college/research/researchproj.html',context)

def conf(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form

    }
    return render(request,'college/research/conf.html',context) 

def awards(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form

    }
    return render(request,'college/research/awards.html',context)               







    