from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import hello, RegisterView, UserListView, ImageUploadView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('image/', ImageUploadView.as_view(), name='image_upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)