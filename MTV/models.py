from statistics import mode
from django.db import models

# Create your models here.

class Blog (models.Model):
    title = models.CharField(max_length= 200)#200제한의 char필트
    body = models.TextField()# 대용량 텍스트
    date = models.DateTimeField(auto_now_add=True) #시간
    photo = models.ImageField(blank= True, null = True, upload_to = 'blog_photo') 
    sound = models.FileField(blank= True, null = True, upload_to = 'blog_sound')

    # ImageField는 이미지를 받는 필드라고 보면 됨 업로드는 blog_photo라는 곳에서 할거라는 뜻
    
    
    def __str__(self): # 이 부분은 내가 쓴 글에 제목이 타이틀로 나오게 함 
        return self.title