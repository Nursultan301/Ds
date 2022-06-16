from django.urls import path

from post.views import Areas, ContactForm, GalleryView

urlpatterns = [
    path('', Areas.as_view(), name="home"),
    path('contact/', ContactForm.as_view(), name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery')
]