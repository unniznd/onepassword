
from django.contrib import admin
from django.urls import path
from onepassword import views as onepasswordviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',onepasswordviews.main,name='onepassword'),
    path('howitworks/',onepasswordviews.howitworks,name='howitworks')
]
