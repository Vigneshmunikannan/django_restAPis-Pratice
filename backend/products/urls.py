from django.urls import path

from .import views
urlpatterns=[
     path('',views.Product_create_view),
     path('alldata/',views.Product_listcreate_view),
    path('<int:pk>/',views.Product_detail_view),
    path('<int:pk>/update/',views.Product_update_view),
    path('<int:pk>/delete/',views.Product_destroy_view)
]