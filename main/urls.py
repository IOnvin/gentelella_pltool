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

    path('subscriptionextract/', views.SubscriptionProductCreateView.as_view(), name='sub_extract'),
    path('subscriptionsw/', views.SubscriptionSW.as_view(), name='sub_calc'),
    path('listsubscription/', views.AddProductListView.as_view(), name='sub_list'),
    path('<int:id>/update2/', views.AddProductUpdateView.as_view(), name='update_prod'),
    path('<int:id>/sub_delete/', views.AddProductDeleteView.as_view(), name='sub_delete'),

    # Perpetual
    path('schedule_perp/', views.list_and_create, name='schedule_perp'),
    path('perpetual_add/', views.PerpetualProductCreateView.as_view(), name='perpetual_add'),
    path('perpetuallist/', views.PerpetualProductListView.as_view(), name='perpetual_list'),
    path('<int:id>/update_perp/', views.PerpetualProductUpdateView.as_view(), name='update_perp'),
    path('<int:id>/delete_perp/', views.PerpetualProductDeleteView.as_view(), name='delete_perp'),
    path('perpsw/', views.PerpetualSW.as_view(), name='perpetual_sw'),


    path('Mod1View/', views.Mod1View.as_view(), name='Mod1View'),
    path('Mod2View/', views.Mod2View, name='Mod2View'),


]
