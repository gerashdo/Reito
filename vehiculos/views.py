from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Vehiculo
from django.views.generic.edit import CreateView
from .forms import Vehiculos_editar, VehiculosForm
from django.urls import reverse_lazy
from usuarios.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# This class is used to create a new vehicle and has the validation
# to check that the user is logged in first


class VehiculoCrear(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "nuevo_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

    # This method is used to obtain the id of the logged in user since
    # in the front end this id is required for the creation of a vehicle because
    # this id is a foreign key of the vehicle
    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, id=self.request.user.id)
        form.instance.id_usuario = usuario
        return super().form_valid(form)
    
    
# This  method has the function to update the data of a car

@login_required
def editar_vehiculo(request):
    # Search current user.
    usuario = get_object_or_404(Usuario, id=request.user.id)
    vehiculo = Vehiculo.objects.filter(id_usuario=usuario).first()
    
    if request.method == "POST":
        form = Vehiculos_editar(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu vehiculo se ha actualizado")
            return redirect("usuarios:ver_mi_cuenta")
    form = Vehiculos_editar(instance=vehiculo)
    context = {
        "form": form,
        "vehiculo": vehiculo
    }
    return render(request, "editar_vehiculo.html", context)
    
    
    
# This method has the function to delete a car

def eliminar_vehiculo(request, pk):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    vehiculo = get_object_or_404(Vehiculo, id=pk, id_usuario=usuario).first()
    
    if request.method == "POST":
        vehiculo.delete()
        messages.success(request, "Tu Vehículo se ha eliminado con éxito.")
        return redirect('usuarios:ver_mi_cuenta')
        
    

# This  method has the function to  show  the data of a car

@login_required
def ver_vehiculo(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    vehiculo = Vehiculo.objects.filter(id_usuario=usuario).first()
    context = {
        'usuario': usuario,
        'vehiculo': vehiculo
    }
    return render(request, "detalle_vehiculo.html", context)
    
    
    
