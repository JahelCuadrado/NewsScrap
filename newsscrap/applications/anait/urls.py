from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.AnaitNewsCrud, 'anait-news')

urlpatterns = router.urls