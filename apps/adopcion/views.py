from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.adopcion.forms import SolicitudForm, PersonaForm, AdopcionForm
from apps.adopcion.models import Solicitud, Persona
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class SolicitudList(ListView):
    model = Solicitud
    template_name = "solicitud/solicitud_list.html"
    context_object_name = "solicitudes"

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    second_form_class = PersonaForm
    template_name = "solicitud/solicitud_form.html"
    success_url = reverse_lazy("adopcion:solicitud_listar")

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.form_class(self.request.GET)
        if "form2" not in context:
            context["form2"] = self.second_form_class(self.request.GET)  # Usar 'second_form_class'
        return context

    def post(self, request, *args, **kwargs):  # Corregido 'delf' a 'self'
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)  # Corregido 'request.PSOT' a 'request.POST'
        
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()  # Guardamos la persona asociada a la solicitud
            solicitud.save()  # Guardamos la solicitud
            messages.success(request, 'Solicitud exitosamente creada')
            return HttpResponseRedirect(self.get_success_url())  # Redirigimos al éxito
        else:
            messages.info(request, 'Algunos campos de la solicitud requieren ser llenados')
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    second_form_class = PersonaForm
    template_name = "solicitud/solicitud_form.html"
    success_url = reverse_lazy("adopcion:solicitud_listar")  # Redirige al listado de solicitudes

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        #pk = get_list_or_404(self.kwarg, "pk")
        pk = self.kwargs.get('pk')  # Obtiene el valor del parámetro 'pk'
        solicitud = self.get_object()  # Obtiene la instancia de la solicitud
        persona = solicitud.persona  # Obtiene la persona asociada a la solicitud
        if "form" not in context:
            context["form"] = self.form_class(instance=solicitud)
        if "form2" not in context:
            context["form2"] = self.second_form_class(instance=persona)
        context["id"] = pk  # Puedes pasar el ID de la solicitud si lo necesitas
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_solicitud = kwargs["pk"]
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = solicitud.persona  # Obtener la persona asociada a la solicitud
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()  # Guarda los cambios en la solicitud
            form2.save()  # Guarda los cambios en la persona asociada
            messages.success(request, 'Solicitud exitosamente creada')
            return HttpResponseRedirect(self.success_url)
        messages.info(request, 'Algunos campos de la solicitud requieren ser llenados')
        context = self.get_context_data()
        return self.render_to_response(context)

class SolicitudDelete(SuccessMessageMixin, DeleteView):
    model = Solicitud
    template_name = "solicitud/solicitud_delete.html"
    success_url = reverse_lazy("adopcion:solicitud_listar")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Solicitud eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

## Adopciones view

class AdopcionList(ListView):
    model = Solicitud
    template_name = "adopcion/adopcion_list.html"
    context_object_name = "adopciones"

class AdopcionCreate(SuccessMessageMixin,CreateView):
    model = Solicitud
    form_class = AdopcionForm
    template_name = "adopcion/adopcion_form.html"
    success_url = reverse_lazy("adopcion:adopcion_listar")
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Adopcion registrada exitosamente")
        return super().form_valid(form)

class AdopcionUpdate(SuccessMessageMixin,UpdateView):
    model = Solicitud
    form_class = AdopcionForm
    template_name = "adopcion/adopcion_form.html"
    success_url = reverse_lazy("adopcion:adopcion_listar")  # Redirige al listado de solicitudes
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Adopcion editada exitosamente")
        return super().form_valid(form)
    
class AdopcionDelete(SuccessMessageMixin,DeleteView):
    model = Solicitud
    template_name = "adopcion/adopcion_delete.html"
    success_url = reverse_lazy("adopcion:adopcion_listar")
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Adopcion eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

## vistas de personas

class PersonaList(ListView):
    model = Persona
    template_name = "persona/persona_list.html"
    context_object_name = "form"

class PersonaCreate(SuccessMessageMixin,CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona/persona_form.html"
    success_url = reverse_lazy("adopcion:persona_listar")
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Persona regietrada exitosamente")
        return super().form_valid(form)

class PersonaUpdate(SuccessMessageMixin,UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona/persona_form.html"
    success_url = reverse_lazy("adopcion:persona_listar")  # Redirige al listado de solicitudes
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Persona editada exitosamente")
        return super().form_valid(form)

class PersonaDelete(SuccessMessageMixin,DeleteView):
    model = Persona
    template_name = "persona/persona_delete.html"
    success_url = reverse_lazy("adopcion:persona_listar")
    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Persona eliminada exitosamente")
        return super().form_valid(form)

# Solicitud function version

def solicitud_list(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "solicitud/solicitud_list.html", {"solicitudes": solicitudes})

def solicitud_create(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        form2 = PersonaForm(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            persona = form2.save()
            solicitud.persona = persona
            solicitud.save()
            messages.success(request, "Solicitud registrada exitosamente")
            return redirect(reverse_lazy("adopcion:f_solicitud_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = SolicitudForm()
        form2 = PersonaForm()
    return render(request, "solicitud/solicitud_form.html", {"form": form, "form2": form2})

def solicitud_update(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    persona = solicitud.persona
    print(persona)
    if request.method == "POST":
        form = SolicitudForm(request.POST, instance=solicitud)
        form2 = PersonaForm(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Solicitud exitosamente editada")
            return redirect(reverse_lazy("adopcion:f_solicitud_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = SolicitudForm(instance=solicitud)
        form2 = PersonaForm(instance=persona)
    return render(request, "solicitud/solicitud_form.html", {"form": form, "form2": form2})

def solicitud_delete(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == "POST":
        solicitud.delete()
        messages.success(request, "Solicitud exitosamente eliminada")
        return redirect(reverse_lazy("adopcion:f_solicitud_listar"))
    return render(request, "solicitud/solicitud_delete.html", {"object": solicitud})

# Adopciones Views version fuction

def adopcion_list(request):
    adopciones = Solicitud.objects.all()
    return render(request, "adopcion/adopcion_list.html", {"adopciones": adopciones})

def adopcion_create(request):
    if request.method == "POST":
        form = AdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Adopcion exitosamente registrada")
            return redirect(reverse_lazy("adopcion:f_adopcion_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = AdopcionForm()
    return render(request, "adopcion/adopcion_form.html", {"form": form})

def adopcion_update(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == "POST":
        form = AdopcionForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, "Adopcion exitosamente editada")
            return redirect(reverse_lazy("adopcion:f_adopcion_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = AdopcionForm(instance=solicitud)
    return render(request, "adopcion/adopcion_form.html", {"form": form})

def adopcion_delete(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == "POST":
        solicitud.delete()
        messages.success(request, "Adopcion exitosamente eliminada")
        return redirect(reverse_lazy("adopcion:f_adopcion_listar"))
    return render(request, "adopcion/adopcion_delete.html", {"object": solicitud})

# Persona Views
def persona_list(request):
    personas = Persona.objects.all()
    return render(request, "persona/persona_list.html", {"form": personas})

def persona_create(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Persona exitosamente registrada")
            return redirect(reverse_lazy("adopcion:f_persona_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = PersonaForm()
    return render(request, "persona/persona_form.html", {"form": form})

def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, "Persona exitosamente editada")
            return redirect(reverse_lazy("adopcion:f_persona_listar"))
        else:
            messages.info(request, "Existen campos faltantes o incorrectos")
    else:
        form = PersonaForm(instance=persona)
    return render(request, "persona/persona_form.html", {"form": form})

def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        persona.delete()
        messages.success(request, "Persona exitosamente eliminada")
        return redirect(reverse_lazy("adopcion:f_persona_listar"))
    return render(request, "persona/persona_delete.html", {"persona": persona})

