from .import views
from django.urls import path
app_name='MLapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('form/',views.index,name='form'),
    path('load-courses/',views.load_courses,name="ajax_load_courses"),
    path('success/',views.submit,name='submit')

]



