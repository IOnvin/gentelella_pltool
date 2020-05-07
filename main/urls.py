from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('404/', views.errorpage, name='404'),
    path('tables_dynamic/', views.tables_dynamic, name='tables_dynamic'),
    path('new_quote/', views.new_quote, name='new_quote'),
    path('add_quote/', views.AddQuoteCreateView.as_view(), name='add_quote'),
    path('<int:id>/', views.AddQuoteDetailView.as_view(), name='detail_quote'),
    path('list_quote/', views.AddQuoteListView.as_view(),name='list_quote'),
    path('p&l_details/', views.pl_details, name='p&l_details'),
    path('demo_quote/', views.AddQuoteCreate2View.as_view(), name='demo_quote'),
    path('<int:id>/update/', views.AddQuoteUpdateView.as_view(), name='update_quote'),
    path('<int:id>/delete/', views.AddQuoteDeleteView.as_view(), name='delete_quote'),
    path('subscription/', views.SubscriptionProductCreateView.as_view(), name='sub_prod')
]
