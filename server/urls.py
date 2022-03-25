
from django.contrib import admin
from django.urls import path
from onepassword import views as onepasswordviews
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',onepasswordviews.main,name='onepassword'),
    path('howitworks/',onepasswordviews.howitworks,name='howitworks'),
    
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
handler404 = onepasswordviews.page_not_found
handler500 = onepasswordviews.internal_error