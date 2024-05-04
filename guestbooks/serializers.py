from rest_framework import serializers
from .models import Guestbook

class GuestbookListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guestbook
    exclude = ['content', 'password']

class GuestbookDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guestbook
    exclude = ['password']