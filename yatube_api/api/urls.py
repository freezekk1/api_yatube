"""URL routes for API endpoints and docs."""

from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

schema_view = get_schema_view(
    title='Yatube API',
    description='Учебный API для постов, групп и комментариев.',
    version='1.0.0',
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view, name='schema'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redoc',
    ),
]
