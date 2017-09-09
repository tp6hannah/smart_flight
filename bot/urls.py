from django.conf.urls import include, url
from .views import bot
urlpatterns = [url(r'^webhook', bot.as_view())]
