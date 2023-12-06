from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dami_app'

urlpatterns = [
    # 유저
    path('', views.main, name='UserMain'),

    # 로그인&&아웃
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main:UserMain'), name='logout'),
    
    # 회원가입
    path('register/', views.register, name='register'),

    # 관리자
    path('admin_main/', views.admin_main, name='admin_main'),  # [관리자] 메인 페이지
    path('admin_user_list/', views.admin_user_list, name='admin_user_list'),  # [관리자] 유저 정보 관리 리스트
    path('admin_user_delete/<int:user_id>/', views.admin_user_delete, name='admin_user_delete'),  # [관리자] 유저 정보 삭제
    path('admin_user_modify/<int:user_id>/', views.admin_user_modify, name='admin_user_modify'),  # [관리자] 유저 정보 수정    


    path('usertype/', views.view_User_type, name='view_User_type'),
]
