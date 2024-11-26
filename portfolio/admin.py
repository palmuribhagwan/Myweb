from django.contrib import admin
from .models import Popup,desktop_img,mobile_img,greeting,home_img,home_pgh,footer,education,experience,Responsibility,Blog_header,Blog
from .models import contact,email_host,contact_map,Nav_Header,resume_header,Skill_title,skill,content,Resume_pdf,main_head_project,project,project_ul,main_head_certificate,certificate,main_head_achievement,achievement

@admin.register(contact,Popup,desktop_img,mobile_img,greeting,home_img,home_pgh,footer,education,experience,Responsibility,Blog_header,Blog)
class Admin(admin.ModelAdmin):
   list_display = ['id'] 

@admin.register(email_host,contact_map,Nav_Header,resume_header,Skill_title,skill,content,Resume_pdf,main_head_project,project,project_ul,main_head_certificate,certificate,main_head_achievement,achievement)
class sAdmin(admin.ModelAdmin):
   list_display = ['id'] 
