from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tento_shop_project.products.api.views import search

urlpatterns = [
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    # Grappelli URLS
    path("grappelli/", include("grappelli.urls")),
    path("grappelli-docs/", include("grappelli.urls_docs")),  # grappelli docs URLS
    # Django Admin, use {% url 'admin:index' %}
    path("admin/", admin.site.urls),
    # User management
    path("users/", include("tento_shop_project.users.urls", namespace="users")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path(settings.ADMIN_URL, admin.site.urls),
)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("auth-token/", obtain_auth_token),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path("api/products/search/", search, name="product-search")
    # path("api/cart/", include("tento_shop_project.cart.api.urls", namespace="cart")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

admin.site.site_header = "Tento Shop Admin"
admin.site.site_title = "Tento Shop Admin Portal"
admin.site.index_title = "Welcome to Tento Shop Admin Portal"
