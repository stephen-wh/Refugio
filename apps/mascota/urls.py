from django.conf.urls import url
from apps.mascota.views import index, mascota_create, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
urlpatterns = [
    #version de clases
    url(r'^$', index, name="index"),
    url(r'^mascota/nuevo/$', MascotaCreate.as_view(), name="mascota_crear"),
    url(r'^mascota/listar/$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^mascota/editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^mascota/eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),
    #version de funciones
    url(r'^mascota/f_nuevo/$', mascota_create, name="f_mascota_crear"),
    url(r'^mascota/f_listar/$', mascota_list, name='f_mascota_listar'),
    url(r'^mascota/f_editar/(?P<pk>\d+)/$', mascota_edit, name='f_mascota_editar'),
    url(r'^mascota/f_eliminar/(?P<pk>\d+)/$', mascota_delete, name='f_mascota_eliminar'),
]