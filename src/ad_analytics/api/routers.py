from rest_framework import routers

from .endpoint import *


router = routers.SimpleRouter()


router.register(r'clicks', ClickViewSet, basename='clicks')
router.register(r'impressions', ImpressionViewSet, basename='impressions')
