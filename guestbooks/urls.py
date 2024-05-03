from django.urls import path
from guestbooks.views import *

urlpatterns = [
    path('', GuestbookList.as_view(), name='guestbook_list'),
    path('<int:id>/', GuestbookDetail.as_view(), name='guestbook_detail')
]