"""Defines URL patterns for learning_logs."""

from xml.etree.ElementInclude import include
from django.urls import path

from learning_log.accounts import admin

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.Topic, name='topic'),

    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('learning_logs.urls')),
]