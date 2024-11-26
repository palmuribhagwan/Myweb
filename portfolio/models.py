from django.db import models
from colorfield.fields import ColorField
class Popup(models.Model):
    Pop_Name = models.CharField(max_length=50)
    popup_message=models.CharField(max_length=50)
    def __str__(self):
        return self.Pop_Name
class desktop_img(models.Model):
    image=models.ImageField(upload_to='desktop')
class mobile_img(models.Model):
    image=models.ImageField(upload_to='mobile')
class greeting(models.Model):
    header=models.TextField()
    message=models.TextField()
    def __str__(self):
        return self.header
class home_img(models.Model):
    image=models.ImageField(upload_to='images')
class home_pgh(models.Model):
    paragraph=models.TextField()
class footer(models.Model):
    name=models.CharField(max_length=20,null=True, blank=True)
    mail=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    linkedin_link=models.TextField(null=True, blank=True)
    insta_link=models.TextField(null=True, blank=True)
    github_link=models.TextField(null=True, blank=True)
    whatsapp_No=models.TextField(null=True, blank=True)
    
class education(models.Model):
    college=models.TextField()
    Degree=models.TextField()
    Branch=models.CharField(max_length=50,null=True, blank=True)
    university=models.CharField(max_length=50,null=True, blank=True)
    start_date=models.DateField(auto_now=False,null=True, blank=True)
    end_date =models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    about=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.college
    
class experience(models.Model):
    profession=models.TextField()
    company=models.TextField()
    start_date=models.DateField(auto_now=False,)
    end_date =models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    def __str__(self):
        return self.company

class Responsibility(models.Model):
    company=models.ForeignKey(experience,on_delete=models.CASCADE) 
    responsibility=models.TextField()
    def __str__(self):
        return self.responsibility

class Skill_title(models.Model):
    Title=models.TextField()
    def __str__(self):
        return self.Title

class skill(models.Model):
    title=models.ForeignKey(Skill_title, on_delete=models.CASCADE,related_name='skills')
    list=models.TextField()
    def __str__(self):
        return self.list
 
class content(models.Model):
    text=models.TextField()    
 
class Resume_pdf(models.Model):
    pdf=models.FileField(upload_to='resume')    
    
class main_head_project(models.Model):
    desk_image=models.ImageField(upload_to='images',null=True, blank=True)
    moble_image=models.ImageField(upload_to='images',null=True, blank=True)
    Title =models.TextField(null=True, blank=True)  
    paragraph=models.TextField(null=True, blank=True) 
    
class project(models.Model):
    image=models.ImageField(upload_to='images/',null=True, blank=True)
    video=models.FileField(upload_to='videos/',null=True, blank=True)
    view_imgvid_left=models.BooleanField(default=False)
    view_imgvid_Right=models.BooleanField(default=True)
    project_title=models.TextField()
    description=models.TextField(null=True, blank=True)
    outcome=models.TextField(null=True, blank=True)
    ul_head=models.TextField(null=True, blank=True)
    link=models.TextField(null=True, blank=True)
    source_code=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.project_title
    
class project_ul(models.Model):
    Project=models.ForeignKey(project, on_delete=models.CASCADE,related_name='project')
    list_context=models.TextField()
    
class main_head_certificate(models.Model):
    desk_image=models.ImageField(upload_to='images',null=True, blank=True)
    moble_image=models.ImageField(upload_to='images',null=True, blank=True)
    Title =models.TextField(null=True, blank=True)  
    paragraph=models.TextField(null=True, blank=True) 
    
class certificate(models.Model):
    image=models.ImageField( upload_to='images/',)
    title=models.TextField()
    about=models.TextField()
    def __str__(self):
        return self.title
    
class main_head_achievement(models.Model):
    desk_image=models.ImageField(upload_to='images',null=True, blank=True)
    moble_image=models.ImageField(upload_to='images',null=True, blank=True)
    Title =models.TextField(null=True, blank=True)  
    paragraph=models.TextField(null=True, blank=True) 
    
class achievement(models.Model):
    image=models.ImageField( upload_to='images/',)
    title=models.TextField()
    about=models.TextField()
    def __str__(self):
        return self.title
    
class Blog_header(models.Model):
    desk_image=models.ImageField(upload_to='images',null=True, blank=True)
    moble_image=models.ImageField(upload_to='images',null=True, blank=True)
    Title =models.TextField(null=True, blank=True)  
    paragraph=models.TextField(null=True, blank=True)
    
class Blog(models.Model):
    title=models.TextField()
    image=models.ImageField(upload_to='images/')
    paragaph=models.TextField()
    
class resume_header(models.Model):
    image=models.ImageField(upload_to='images',null=True, blank=True)
    Title =models.TextField(null=True, blank=True)  
    paragraph=models.TextField(null=True, blank=True)
    
class Nav_Header(models.Model):
    Title=models.TextField()
    Blogs=models.BooleanField()
    Resume=models.BooleanField()
    Projects=models.BooleanField()
    certificates=models.BooleanField()
    Achievements=models.BooleanField()
    contact=models.BooleanField()
    search=models.BooleanField()
    header_color=ColorField(default='#FFFFFF')
    sidebar_color=ColorField(default='#FFFFFF')
           
class contact_map(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField() 
    
class contact(models.Model):
    name = models.TextField()
    email = models.EmailField(max_length=254)
    subject =  models.TextField()
    message =  models.TextField()
    
class email_host(models.Model):
    recive_mail_to=models.EmailField(max_length=254) 