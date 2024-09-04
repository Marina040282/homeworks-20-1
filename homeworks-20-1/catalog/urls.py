from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from views import IndexListView, contacts
from apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
                  path('', IndexListView.as_view(), name='index'),  # вывод главной страницы
                  path('contacts', contacts, name='contact'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Это добавляется один раз на проект
