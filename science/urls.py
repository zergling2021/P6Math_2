from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns = [
#    path('', views.index, name='index'),
#]
from . import views
app_name = 'science'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('science_report/', views.ScienceReportView.as_view(), name='science_report'),
    path('science_mcq/', views.ScienceMCQView.as_view(), name='science_mcq'),
    path('science_open/', views.ScienceOpenView.as_view(), name='science_open'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('generate_science_report', views.generate_science_report, name='generate_science_report'),
    path('science_reportresult/', views.ScienceReportresultView.as_view(), name='science_reportresult'),
    path('english_report/', views.EnglishReportView.as_view(), name='english_report'),
    path('english_mcq/', views.EnglishMCQView.as_view(), name='english_mcq'),
    path('english_open/', views.EnglishOpenView.as_view(), name='english_open'),
    path('english_reportresult/', views.EnglishReportresultView.as_view(), name='english_reportresult'),
    path('generate_english_report', views.generate_english_report, name='generate_english_report'),

]

urlpatterns += staticfiles_urlpatterns()