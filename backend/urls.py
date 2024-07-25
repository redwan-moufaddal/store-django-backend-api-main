
from django.contrib import admin
from django.urls import path,include
from base.views import *
from home import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", create_user_view, name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/home/",views.home_page_data,name="home page"),
    path("api/shop/",views.shop_page_data,name="shop page"),
    path("api/contact/",views.contact_page_data,name="contact page"),
    path('api/product/detail/<int:pk>/', views.one_product_data, name='one product data'),
    path('api/products-by-category/<str:category>/', views.products_by_category, name='products_by_category'),
    path("api-auth/", include("rest_framework.urls")),
]
