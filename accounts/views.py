from django.shortcuts import render , redirect , get_object_or_404
from .forms import (UserRegistrationForm,
				    UserEditProfileForm, 
				    UserEditForm)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile , Contact
from images.common.decorators import ajax_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from actions.utils import create_action
from actions.models import Action
from django.contrib.contenttypes.models import ContentType





def user_registration(request):

	if request.method == 'POST':

		form = UserRegistrationForm(data=request.POST)

		if form.is_valid():

			cd = form.cleaned_data

			new_user = form.save(commit=False)

			new_user.set_password(cd['password2'])
			new_user.save()
			create_action(new_user , 'has created an account')
			UserProfile.objects.create(user=new_user)


			return redirect("login")

	else:

		form = UserRegistrationForm()


	return render(request , "register.html" , {'form':form})



@login_required
def dashboard(request):

	
	actions = Action.objects.exclude(user__id=request.user.id)

	following_ids = request.user.following.values_list('id',
													   flat=True)

	if following_ids:

		actions = actions.filter(user__id__in=following_ids)
		actions = actions[:10]
		
	return render(request , 'dash.html' , {'actions':actions})



@login_required
def user_edit_profile(request):

	created = None

	if request.method == 'POST':

		user_form = UserEditForm(data=request.POST,
							     instance=request.user)

		profile_form = UserEditProfileForm(data=request.POST,
								   		   files=request.FILES,
								   		   instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():

			profile_form.save()
			
			user_form.save()

			created = True

			return render(request , 'dash.html' , {'created':created})

	else:

		profile_form = UserEditProfileForm()
		user_form = UserEditForm(instance=request.user)


	return render(request , 'edit_profile.html' , {'profile_form':profile_form,
												   'user_form':user_form})



@login_required
def users(request):

	users = User.objects.filter(is_active=True).exclude(id=request.user.id)

	return render(request , 'users.html' , {'users':users})



@login_required
def user_detail(request , username):

	user = get_object_or_404(User , username=username , is_active=True)

	return render(request , 'user_detail.html' , {'user':user})




@require_POST
@ajax_required
@login_required
def follow(request):


	user_id = request.POST.get('id')
	action = request.POST.get('action')

	if user_id and action:

		try:

			user = User.objects.get(id=user_id)

			if action == 'follow':

				
						

				Contact.objects.get_or_create(user_from=request.user,
											  user_to=user)

				create_action(request.user , "is following" , user)


			else:

				Contact.objects.filter(user_from=request.user,
									   user_to=user).delete()

				user_ct = ContentType.objects.get_for_model(user)

				Action.objects.get(user__id=request.user.id,
								   verb="is following",
								   target_ct=user_ct,
								   target_id=user.id).delete()

			



			return JsonResponse({'status':'ok'})

		except User.DoesNotExist:

			return JsonResponse({'status':'ko'})

	return JsonResponse({'status':'ko'})
	

@login_required
def followers(request):


	followers = request.user.followers.all()

	return render(request , 'followers.html' , {'followers':followers})



@login_required
def followings(request):

	followings = request.user.following.all()

	return render(request , 'followings.html' , {'followings': followings})



@require_POST
@login_required
def unfollow(request , username):


	user = get_object_or_404(User , username=username , is_active=True)

	Contact.objects.filter(user_from__id=request.user.id,
						   user_to__id=user.id).delete()

	user_ct = ContentType.objects.get_for_model(user)
	Action.objects.filter(user__id=request.user.id,
						  verb='is following',
						  target_ct=user_ct,
						  target_id=user.id).delete()

	return redirect('followings')



@require_POST
@login_required
def remove_follower(request , username):

	user = get_object_or_404(User , username=username , is_active=True)

	Contact.objects.filter(user_from__id=user.id,
						   user_to__id=request.user.id).delete()

	user_ct = ContentType.objects.get_for_model(request.user)
	Action.objects.filter(user__id=user.id,
						  verb="is following",
						  target_ct=user_ct,
						  target_id=request.user.id).delete()


	return redirect('followers')


'''
@require_POST
@login_required
def accept_follow(request, username, user_id):

	user = get_object_or_404(User , username=username , id=user_id ,  is_active=True)

	Contact.objects.get_or_create(user_from__id=user.id,
								  user_to__id=request.user.id)

	create_action(user , "is following" , request.user)

	return redirect('dashboard')



@require_POST
@login_required
def refuse_follow(request , username):

	user = get_object_or_404(User , username=username , is_active=True)
	user_ct = ContentType.objects.get_for_model(request.user)
	Action.objects.filter(user__id=user.id,
						  verb='has requested to follow',
						  target_ct=user_ct,
						  target_id=request.user.id).delete()


	return redirect('dashboard')
'''
