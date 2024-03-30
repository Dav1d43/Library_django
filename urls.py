from django.contrib import admin
from django.urls import path, include
from reader.views import reader_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reader_info, name='reader_info'),
    path('<int:book_id>/', include('book.urls')),
]