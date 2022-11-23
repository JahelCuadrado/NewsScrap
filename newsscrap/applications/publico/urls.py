from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PublicoNewsCrud, 'publico-news')

urlpatterns = router.urls