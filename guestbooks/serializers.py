from rest_framework import serializers
from .models import Guestbook

class GuestbookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guestbook
    exclude = ['password']

class GuestbookSecureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guestbook
    exclude = []