from django.conf.urls import url
from apps.usuario.views import RegistroUsuario
urlpatterns = [
    url(r'^$', RegistroUsuario.as_view(), name="usuario_crear"),
    # url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    # url(r'^editar/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='mascota_editar'),
    # url(r'^eliminar/(?P<pk>\d+)$', MascotaDelete.as_view(), name='mascota_eliminar'),
]