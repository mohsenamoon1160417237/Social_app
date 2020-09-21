from django.urls import path
from . import views


urlpatterns = [

	path('best_images/' , views.most_liked_images , name='most_liked_images'),
	path('' , views.image_post , name='image_post'),
	path('delete/<int:image_id>/<slug:image_slug>/' , views.image_delete , name='image_delete'),
	path('all/' , views.images , name='images'),
	path('<slug:image_slug>/<int:image_id>/' , views.image_detail , name='image_detail'),
	path('like/' , views.image_like , name='image_like'),
	

]