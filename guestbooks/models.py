from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성 일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 일시", auto_now=True)

    class Meta:
        abstract = True

class Guestbook(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=30)
    writer = models.CharField(verbose_name="작성자", max_length=20)
    content = models.TextField(verbose_name="내용")
    password = models.CharField(verbose_name="비밀번호", max_length=20)