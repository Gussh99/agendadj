from django.urls import path, re_path, include

from . import views

app_name ='persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonas.as_view(),
        name='personas'
    ),
    path(
        'api/persona/lista/',
        views.PersonListApiView.as_view(),
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista'
    ),
    path(
        'api/persona/search/<kword>/',
        views.PersonSearchApiView.as_view(),
    ),
    path(
        'api/persona/create/',
        views.PersonCreateView.as_view(),
    ),
    path(
        'api/persona/detail/<pk>/',
        views.PersonaDetailView.as_view(),
        name='detalle'
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonaDeleteView.as_view(),
    ),
    path(
        'api/persona/update/<pk>/',
        views.PersonaUpdateView.as_view(),
    ),
    path(
        'api/persona/retrieve-update/<pk>/',
        views.PersonaRetrieveUpdateView.as_view(),
    ),
    #api normal 
    path(
        'api/personas/',
        views.PersonApiLIsta.as_view(),
    ),
    path(
        'api/reuniones/',
        views.ReunionApiLIsta.as_view(),
    ),
    path(
        'api/reuniones-link/',
        views.ReunionApiLIstaLink.as_view(),
    ),
    path(
        'api/persona/pagination/',
        views.PersonApiLIstaPagination.as_view(),
    ),
    path(
        'api/reuniones/jobs/',
        views.ReunionCountJob.as_view(),
    )
]