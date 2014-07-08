from django.conf.urls import patterns, url
from ReactComments import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomePageView.as_view(), name='index'),
)
