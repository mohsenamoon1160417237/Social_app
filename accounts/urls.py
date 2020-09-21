from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

	
	
	path('remove_follower/<username>/' , views.remove_follower , name='remove_follower'),
	path('unfollow/<username>/' , views.unfollow , name='unfollow'),
	path('followers/' , views.followers , name='followers'),
	path('followings/' , views.followings , name='followings'),
	path('' , views.dashboard , name='dashboard'),
	path('users/' , views.users , name='users'),
	path('user/<username>/' , views.user_detail , name='user_detail'),
	path('follow/' , views.follow , name='follow'),
	path('edit/' , views.user_edit_profile , name='edit_profile'),

	path('register/' , views.user_registration , name='register'),
	path('login/' , auth_views.LoginView.as_view() , name='login'),
	path('logout/' , auth_views.LogoutView.as_view() , name='logout'),
	
	path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change'),
	path('password_change_done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'),
	
	path('password_reset/' , auth_views.PasswordResetView.as_view(),
							 name="password_reset"),

	path('password_reset_done/' , auth_views.PasswordResetDoneView.as_view(),
								  name='password_reset_done'),

	path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(),
									 name='password_reset_confirm'),

	path('reset/done/' , auth_views.PasswordResetCompleteView.as_view(),
						 name='password_reset_complete'),
						 	

] 