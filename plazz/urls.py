import os
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
import plazz
from . import views

urlpatterns = [
    # ex: /location/
    path('', views.index, name='index'),
    # ex: /location/5/
    path('filters/', views.filters, name='filters'),
    # # ex: /location/5/results/
    path('results/', views.results, name='results'),
    # # ex: /location/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

for filename in os.listdir(os.path.join(os.path.dirname(plazz.__file__), "static", "root")):
    urlpatterns.append(path(
        '{0}'.format(filename),
        RedirectView.as_view(url=static('root/{0}'.format(filename))))
    )
