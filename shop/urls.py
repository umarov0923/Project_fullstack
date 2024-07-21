from django.urls import path
from . import views


def search_view(request):
    return render(request, 'shop/search.html')


app_name = 'shop'
urlpatterns = [
    path('', views.product_view, name='products'),
    path('<slug:slug>/', views.product_detail_view, name = 'product_detail'),
    path('search/<slug:slug>/', views.category_list, name = 'category_list'),
    path('search/', search_view, name = 'search-products'),
]