from django.shortcuts import render , get_object_or_404 , redirect
from .forms import ImagePostForm
from django.contrib.auth.decorators import login_required
from .models import Image
from django.http import JsonResponse , HttpResponse
from django.views.decorators.http import require_POST
from .common.decorators import ajax_required
from actions.utils import create_action
from actions.models import Action
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count






@login_required
def image_post(request):


	if request.method == 'POST':

		form = ImagePostForm(data=request.POST,
							 files=request.FILES)

		if form.is_valid():

			cd = form.cleaned_data
			new_image = form.save(commit=False)
			new_image.user = request.user
			new_image.save()


			
			create_action(request.user , "posted image" , target=new_image)

			return redirect('images')

	else:

		form = ImagePostForm()

	return render(request , 'image.html' , {'form':form})



@login_required
def images(request):

	images = Image.objects.filter(user=request.user)
	

	return render(request , 'images.html' , {'images':images})



@login_required
def image_detail(request , image_slug , image_id):

	image = get_object_or_404(Image , slug=image_slug , id=image_id)

	return render(request , 'image_detail.html' , {'image':image})




@ajax_required
@login_required
@require_POST
def image_like(request):

	image_id = request.POST.get('id')
	action = request.POST.get('action')

	if image_id and action:

		try:

			image = Image.objects.get(id=image_id)

			if action == 'like':

				image.users_like.add(request.user)
				
				create_action(request.user , "likes" , image)

			else:

				
				
				image.users_like.remove(request.user)
				image_ct = ContentType.objects.get_for_model(image)
				Action.objects.get(user__id=request.user.id,
									  verb="likes",
									  target_ct=image_ct,
									  target_id=image.id).delete()



		
			return JsonResponse({'status':'ok'})

		except:

			pass

	return JsonResponse({'status':'ko'})





@require_POST
@login_required
def image_delete(request , image_id , image_slug):

	image = get_object_or_404(Image , id=image_id , slug=image_slug , user__id=request.user.id)

	image_ct = ContentType.objects.get_for_model(image)

	Action.objects.get(user__id=request.user.id,
					   verb='posted image',
					   target_ct=image_ct,
					   target_id=image.id).delete()

	image.delete()

	return redirect('images')



@login_required
def most_liked_images(request):


	images = Image.objects.all()
	images = images.annotate(likes=Count('users_like')).order_by('-likes')[:10]


	return render(request , 'most_liked_images.html' , {'images':images})


