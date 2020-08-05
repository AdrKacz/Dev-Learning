from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('logements/', views.LogementListView.as_view(), name='logements'),
	path('logement/<int:pk>', views.LogementDetailView.as_view(), name='logement-detail'),
	path('faq/', views.QuestionReponseListView.as_view(), name='faq'),

	path('informations/', views.informations, name="informations")
]