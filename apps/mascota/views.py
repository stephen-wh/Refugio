from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def index (request):
    return render(request, "mascota/index.html")

def mascota_create(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota exitosamente creada')
            return redirect("mascota:f_mascota_listar")
        else:
            messages.info(request, 'Existen campos faltantes')
    else:
        form = MascotaForm()
    return render(request, "mascota/mascota_form.html", {"form": form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by("-id")
    contexto = {"mascotas": mascota}
    return render(request, "mascota/mascota_list.html", contexto)

class MascotaList(ListView):
    model = Mascota
    template_name = "mascota:mascota_list.html"
    context_object_name = "mascotas"


def mascota_edit(request, pk):
    mascota = get_object_or_404(Mascota, id=pk)
    if request.method == "GET":
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota actualizada exitosamente')
            return redirect("mascota:f_mascota_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    return render(request, "mascota/mascota_form.html", {"form": form})

def mascota_delete(request, pk):
    mascota = get_object_or_404(Mascota, id=pk)
    if request.method == "POST":
        mascota.delete()
        messages.success(request, 'Mascota eliminada exitosamente')
        return redirect("mascota:f_mascota_listar")
    return render(request, "mascota/mascota_delete.html", {"object": mascota})

class MascotaCreate(SuccessMessageMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascota/mascota_form.html"
    success_url = reverse_lazy("mascota:mascota_listar")
    
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Mascota creada exitosamente")
        return super().form_valid(form)

class MascotaUpdate(SuccessMessageMixin, UpdateView):
    # - be for defect object 
    #  model = Mascota
    form_class = MascotaForm
    template_name = "mascota/mascota_form.html"
    # success_url = reverse_lazy("mascota:mascota_listar")

    # personaisa el direccionamiento
    def get_success_url(self):
        return reverse_lazy("mascota:mascota_listar")

    # personalizate form the request in the path
    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Mascota, id=_id)

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Mascota actualizada exitosamente")
        return super().form_valid(form)

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = "mascota/mascota_delete.html"
    success_url = reverse_lazy("mascota:mascota_listar")
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Mascota eliminada exitosamente")
        return super().delete(request, *args, **kwargs)
