from django.shortcuts import render,redirect
from .models import Popup,desktop_img,mobile_img,greeting,home_img,home_pgh,footer,education,experience,main_head_achievement,achievement
from .models import contact,email_host,contact_map,Nav_Header,resume_header,Skill_title,skill,content,Resume_pdf,main_head_project,project,project_ul,main_head_certificate,certificate,Blog_header,Blog
from django.core.mail import send_mail
from django.contrib import messages
def home(request):
    greetings=greeting.objects.all()
    aboutimage=home_img.objects.all()
    home_paragraphs=home_pgh.objects.all()
    footers=footer.objects.all()
    desktop_imgs=desktop_img.objects.all()
    mobile_imgs=mobile_img.objects.all()
    popup=Popup.objects.all()
    Nav_Headers=Nav_Header.objects.all()
    context={
        'greetings':greetings,
        'aboutimages':aboutimage,
        'home_paragraphs':home_paragraphs,
        'footer':footers,
        'desktop_imgs':desktop_imgs,
        'mobile_imgs':mobile_imgs,
        'popup':popup,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'home.html',context)
def Resume_view(request):
    footers=footer.objects.all()
    Education=education.objects.all()
    experiences=experience.objects.all()
    Skill_titles=Skill_title.objects.prefetch_related('skills').all()
    contents=content.objects.all()
    resume_pdf=Resume_pdf.objects.all()
    resume_headers=resume_header.objects.all()
    Nav_Headers=Nav_Header.objects.all()
    context={
        'footer':footers,
        'Education':Education,
        'experiences':experiences,
        'Skill_titles':Skill_titles,
        'contents':contents,
        'Resume_pdf':resume_pdf,
        'resume_header':resume_headers,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'Resume.html',context)

def projects_view(request):
    footers=footer.objects.all()
    main_head_projects=main_head_project.objects.all()
    projects=project.objects.prefetch_related('project').all()
    Nav_Headers=Nav_Header.objects.all()
    context={
        'footer':footers,
        'main_head_project':main_head_projects,
        'project':projects,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'projects.html',context)

def certifications_view(request):
    Nav_Headers=Nav_Header.objects.all()
    footers=footer.objects.all()
    main_head_certificates=main_head_certificate.objects.all()
    certificates=certificate.objects.all()
    context={
        'footer':footers,
        'certificates':certificates,
        'main_head_certificates':main_head_certificates,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'certifications.html',context)

def Achievements_view(request):
    footers=footer.objects.all()
    main_head_achievements=main_head_achievement.objects.all()
    achievements=achievement.objects.all()
    Nav_Headers=Nav_Header.objects.all()
    context={
        'footer':footers,
        'main_head_achievements':main_head_achievements,
        'achievements':achievements,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'achievements.html',context)

def Blog_view(request):
    Nav_Headers=Nav_Header.objects.all()
    footers=footer.objects.all()
    Blog_headers=Blog_header.objects.all()
    Blogs=Blog.objects.all()
    context={
        'footer':footers,
        'Blog_headers':Blog_headers,
        'Blogs':Blogs,
        'Nav_Headers':Nav_Headers
    }
    return render(request,'blogs.html',context)


def contact_view(request):
    Nav_Headers=Nav_Header.objects.all()
    footers=footer.objects.all()
    contact_info =contact_map.objects.first()
    email_hosts=email_host.objects.first()
    if contact_info:
        latitude = contact_info.latitude 
        longitude = contact_info.longitude 
        offset = 0.01
        min_lat = latitude - offset
        max_lat = latitude + offset
        min_lng = longitude - offset
        max_lng = longitude + offset
        context={
        'footer':footers,
        'Nav_Headers':Nav_Headers,
        'contact_info':contact_info,
        'latitude':latitude,
        'longitude':longitude,
        'min_lat': min_lat,
        'max_lat': max_lat,
        'min_lng': min_lng,
        'max_lng': max_lng,
        }
    else:
        context={
            'footer':footers,
            'Nav_Headers':Nav_Headers,
            'contact_info':contact_info,
        }
    if request.method == 'POST':
        if email_hosts:
            if request.method == 'POST':
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                message = request.POST['message']
                send_mail(
                        subject,
                        message,
                        email,
                        [email_hosts.recive_mail_to],  
                        fail_silently=False,
                    )
                contact.objects.create(name=name,email=email,subject=subject,message=message)
                messages.success(request,'Your message has been sent successfully. ')
                return redirect('contact_view')
        else:        
            if request.method == 'POST':
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                message = request.POST['message']
                contact.objects.create(name=name,email=email,subject=subject,message=message)
                messages.success(request,'Your message has been sent successfully. ')
                return redirect('contact_view')
    return render(request,'contact.html',context)
