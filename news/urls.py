from django.urls import path

from .views import NewsViewSet ,FavcategoryViewSet ,CategoryViewSet


from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('news',NewsViewSet)
router.register('cats',CategoryViewSet)
router.register('fcats',FavcategoryViewSet)


urlpatterns = router.urls