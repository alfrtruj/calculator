from django.urls import path
from . import views

urlpatterns = [
    path('quote/input/', views.data_input, name='data_input'),
    path('quote/<int:pk>/', views.data_quote, name='data_quote'),
    path('quote/<int:pk>/edit/', views.data_edit, name='data_edit'),
    path('Piql_order_form.xlsx/', views.download_file, name='download_order'),
    path('', views.data_history, name='data_history'),
    path('200926_piql_prices.pdf/', views.price_list, name='price_list'),
    path('quote/<int:pk>/delete/', views.quote_delete, name='quote_delete'),
    path('signup/', views.signup, name='signup'),
    ]
