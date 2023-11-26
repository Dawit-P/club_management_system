from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
# post views
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('', views.dashboard, name='dashboard'),
path('edit/', views.edit, name='edit'),
path('', include('django.contrib.auth.urls')),  

# #Register
path('register/', views.register, name='register'),

# # change password urls
path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

# # reset password urls
path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

#Member
    # path('members/', member_list, name='member_list'),
    path('members/<int:pk>/', member_detail, name='member_detail'),
    path('members/add/', member_add, name='member_add'),
    path('members/<int:pk>/edit/', member_edit, name='member_edit'),
    path('members/<int:pk>/remove/', member_remove, name='member_remove'),
#Member_list
    path('member_list/', MemberListView.as_view(), name='member_list'),
]