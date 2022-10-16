from django.contrib import admin
from django.urls import path
from aplikasi.views import aplikasi
from evaluasi.views import evaluasi
from home.views import home
from latihan.views import latihan
from materi.views import materi
from profil.views import profil
from video.views import video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplikasi/', aplikasi),
    path('evaluasi/', evaluasi),
    path('home/', home),
    path('latihan/', latihan),
    path('materi/', materi),
    path('profil/', profil),
    path('video/', video)
]
