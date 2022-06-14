from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()

router.register('soumission', views.SoumissionAdminViewset, basename='soumission')
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^soumission/offre/(?P<offre>[^/]+)/$', views.SoumissionGetByOffreView.as_view()),
    re_path(r'^soumission/user/(?P<soumissionnaire>[^/]+)/$', views.SoumissionGetBySoumissionnaireView.as_view()),
    re_path(r'^soumission/lot/(?P<lot>[^/]+)/$', views.SoumissionGetByLotView.as_view()),
    re_path(r'^soumission/getPrix/(?P<soumission>[^/]+)/(?P<prix>[^/]+)/$', views.GetPrixView.as_view())

]
