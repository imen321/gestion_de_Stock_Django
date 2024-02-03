# API/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('fournisseurs', views.FournisseurViewSet)
router.register('produits', views.ProduitViewSet)
router.register('achats', views.AchatViewSet)
router.register('users', views.UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('clients/<int:pk>/', views.ClientDetail.as_view())
    path('prod/count/', views.CountViewSet.as_view(), name='produits-count'),
    path('risk/', views.RiskViewSet.as_view(), name='risk'),
    ]
