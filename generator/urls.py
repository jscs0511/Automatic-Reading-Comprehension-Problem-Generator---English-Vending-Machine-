from django.conf.urls import include, url
from generator import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

app_name = 'generator'

urlpatterns = [
    path('', views.home, name="home"),
    path('Upload_Photo', views.Upload_Photo, name='Upload_Photo'),
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    path('beforeImageCrop/', views.beforeImageCrop),
    path('show_problem', views.show_problem, name='show_problem'),
    path('createCropImage/', csrf_exempt(views.createCropImage)),
    path('ImageCrop/<word>/', views.ImageCrop),
    path('CropToOCR/', views.crop_to_OCR),
    path('show_UserProblem', views.show_UserProblem, name='show_UserProblem'),
    path('OneProblem/<word>/', views.show_OneProblem),
    path('solveProblem/<word>/', views.solve_Problem),
    path('showAnswer', views.show_Answer, name='showAnswer'),
    path('OneBlankNum/<word>/', views.show_OneBlankNum),
    path('ChangeBlankNum/<word>', views.change_BlankNum, name='ChangeBlankNum'),
    path('show_UserBlankNum', views.show_UserBlankNum, name='show_UserBlankNum'),
    path('show_DeveloperInfo', views.show_DeveloperInfo, name='show_DeveloperInfo'),
    path("<id>/", views.scan_img_from_DB),
]