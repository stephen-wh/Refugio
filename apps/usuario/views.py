from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = "usuario/register.html"
    success_url = reverse_lazy("mascota:mascota_listar")

#vista basada en clases
# class UsuarioList(ListView):
#     model = Usuario
#     template_name = "mascota:mascota_list.html"

# class MascotaUpdate(UpdateView):
#     template_name = "mascota/mascota_form.html"
#     success_url = reverse_lazy("mascota:mascota_listar")

# class MascotaDelete(DeleteView):
#     model = Mascota
#     template_name = "mascota/mascota_delete.html"
#     success_url = reverse_lazy("mascota:mascota_listar")
#     template_name = "mascota/mascota_form.html"
#     success_url = reverse_lazy("mascota:mascota_listar")

# class MascotaDelete(DeleteView):
#     model = Mascota
#     template_name = "mascota/mascota_delete.html"
#     success_url = reverse_lazy("mascota:mascota_listar")