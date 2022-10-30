"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MTV import views
from django.conf import settings # 관례 같은거 
from django.conf.urls.static import static # 관례 같은거
urlpatterns = [
    path('admin/', admin.site.urls),
    path('MTV/',include('MTV.urls')),
    path('',views.home, name = 'home'),
    # FORM을 활용한 블로그 객체 
    path('create/',views.create, name = 'create'),
    path('new/',views.new, name = 'new'),
    # 장고용 폼 사용 
    path('formcreate/' , views.formcreate, name = 'formcreate'),
    path('modelformcreate/',views.modelformcreate, name = 'modelformcreate'),
    #디테일패스인데 뒤에 int는 넘겨질 아이디 값을  blog_id에 저장한다는 뜻 
    path('detail/<int:blog_id>', views.detail, name = 'detail'),
    #삭제 버튼 구현하기 
    path('detail/<int:blog_id>/delete/', views.delete, name= 'delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
