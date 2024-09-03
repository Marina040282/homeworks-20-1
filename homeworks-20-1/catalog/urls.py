from django.urls import path

from catalog.views import index, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
                  path('', IndexListView.as_view(), name='index'),  # вывод главной страницы
                  path('contacts/', cache_page(60)(UserDetailView.as_view()), name='contact'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект