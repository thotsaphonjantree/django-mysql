from django.conf.urls import url
from rest_framework import routers
from project.appname.views import StudentViewSet, MajorViewSet,CustomView
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'majors', MajorViewSet)
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls