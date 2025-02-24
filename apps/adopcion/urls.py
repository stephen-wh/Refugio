from django.conf.urls import url
from apps.adopcion.views import PersonaList, PersonaCreate, PersonaDelete, PersonaUpdate, persona_create, persona_list, persona_delete, persona_update, adopcion_update,adopcion_delete,adopcion_create,adopcion_list, solicitud_create, solicitud_list, solicitud_update, solicitud_delete, persona_list, persona_create, persona_delete, persona_update, AdopcionUpdate,AdopcionDelete,AdopcionCreate,AdopcionList, SolicitudCreate, SolicitudList, SolicitudUpdate, SolicitudDelete
urlpatterns = [
    #clases
    url(r'^solicitud/$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/crear/$', SolicitudCreate.as_view(), name="solicitud_crear"),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
    
    url(r'^$', AdopcionList.as_view(), name='adopcion_listar'),
    url(r'^crear/$', AdopcionCreate.as_view(), name="adopcion_crear"),
    url(r'^editar/(?P<pk>\d+)/$', AdopcionUpdate.as_view(), name='adopcion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', AdopcionDelete.as_view(), name='adopcion_eliminar'),

    url(r'^persona/$', PersonaList.as_view(), name='persona_listar'),
    url(r'^persona/crear/$', PersonaCreate.as_view(), name="persona_crear"),
    url(r'^persona/editar/(?P<pk>\d+)/$', PersonaUpdate.as_view(), name='persona_editar'),
    url(r'^persona/eliminar/(?P<pk>\d+)/$', PersonaDelete.as_view(), name='persona_eliminar'),

    #funciones

    url(r'^solicitud/f/$', solicitud_list, name='f_solicitud_listar'),
    url(r'^solicitud/f/crear/$', solicitud_create, name="f_solicitud_crear"),
    url(r'^solicitud/f/editar/(?P<pk>\d+)/$', solicitud_update, name='f_solicitud_editar'),
    url(r'^solicitud/f/eliminar/(?P<pk>\d+)/$', solicitud_delete, name='f_solicitud_eliminar'),
    
    url(r'^f/$', adopcion_list, name='f_adopcion_listar'),
    url(r'^f/crear/$', adopcion_create, name="f_adopcion_crear"),
    url(r'^f/editar/(?P<pk>\d+)/$', adopcion_update, name='f_adopcion_editar'),
    url(r'^f/eliminar/(?P<pk>\d+)/$', adopcion_delete, name='f_adopcion_eliminar'),

    url(r'^persona/f/$', persona_list, name='f_persona_listar'),
    url(r'^persona/f/crear/$', persona_create, name="f_persona_crear"),
    url(r'^persona/f/editar/(?P<pk>\d+)/$', persona_update, name='f_persona_editar'),
    url(r'^persona/f/eliminar/(?P<pk>\d+)/$', persona_delete, name='f_persona_eliminar'),

]