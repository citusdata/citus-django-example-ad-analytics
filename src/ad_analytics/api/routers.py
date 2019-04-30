from rest_framework import routers

from .endpoint import *


router = routers.SimpleRouter()


router.register(r'clicks', ClickViewSet, base_name='clicks')
router.register(r'impressions', ImpressionViewSet, base_name='impressions')
