from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp' # url name이 app마다 겹치는 것 방지

urlpatterns = [
    path('', views.index, name='index'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
