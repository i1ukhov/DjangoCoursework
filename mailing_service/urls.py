from django.urls import path
from django.views.decorators.cache import cache_page

from mailing_service.apps import MailingServiceConfig

from mailing_service.views import NewsletterListView, NewsletterUpdateView, NewsletterDeleteView, NewsletterCreateView, \
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, Homepage, MessageListView, MessageCreateView, \
    MessageUpdateView, MessageDeleteView, NewsletterTryListView, NewsletterDetailView, ClientDetailView, \
    MessageDetailView

app_name = MailingServiceConfig.name

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('newsletters/', NewsletterListView.as_view(), name='newsletters_list'),
    path('newsletters/create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletters/<int:pk>/update', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletters/<int:pk>/detail', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/<int:pk>/delete', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/detail', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='messages_list'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/detail', MessageDetailView.as_view(), name='message_detail'),
    path('messages/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
    path('newsletters/report', NewsletterTryListView.as_view(), name='newsletters_report'),
]
