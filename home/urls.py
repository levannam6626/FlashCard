from django.urls import path
from . import views
urlpatterns = [
    path('',views.gethome,name='home'),
    path('home/',views.gethome,name='home'),
    path('register/', views.register,name='register'),
    path('dangnhap/', views.dangnhap,name='dangnhap'),
    path('themhocphan/', views.themhocphan,name='themhocphan'),
    path('xemdanhsachhocphan/', views.xemdanhsachhocphan,name='xemdanhsachhocphan'),
    path('xemdanhsachhocphan/timkiemhocphan/', views.xemdanhsachhocphan,name='timkiemhocphan'),
    path('dangxuat/', views.dangxuat,name='dangxuat'),
    path('chitiet/<tenhocphan>', views.chitiet, name='chitiet'),
    path('themtudien/<tenhocphan>', views.themtudien, name='themtudien'),
    path('suahocphan/<tenhocphan>', views.suahocphan, name='suahocphan'),
    path('xoahocphan/<tenhocphan>', views.xoahocphan, name='xoahocphan'),
    path('suatudien/<id>', views.suatudien, name='suatudien'),
    path('xoatudien/<id>', views.xoatudien, name='xoatudien'),
]
