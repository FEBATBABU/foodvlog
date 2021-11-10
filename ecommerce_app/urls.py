from django.urls import path
from . import views
app_name='ecommerce_app'
urlpatterns = [

    path('', views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='ProdCatDetail'),
    path('search',views.SearchResult,name='search'),
    ]