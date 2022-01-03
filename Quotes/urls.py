from django.urls import path
from . import views
urlpatterns = [
    path('quotes', views.QuotesList.as_view()),
    path('quote/<int:id>', views.QuotesGet.as_view())
]