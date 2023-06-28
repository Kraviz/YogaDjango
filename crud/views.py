from django.shortcuts import render, redirect, reverse
from crud.forms import ProductForm
from crud.models import Producto
# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            titulo = form.cleaned_data.get('titulo')
            precio = form.cleaned_data.get('precio')
            stock = form.cleaned_data.get('stock')
            img = form.cleaned_data.get('img')
            descripcion = form.cleaned_data.get('descripcion')
            nuevo_prod = Producto.objects.create(
                id = id,
                titulo = titulo,
                precio = precio,
                stock = stock,
                img = img
            )
            nuevo_prod.save()
            return redirect(reverse('tienda') + '?creado')
        else:
            print(form.errors)
            return redirect(reverse('tienda') + '?error')
    else:    
        form = ProductForm()
        context = {'form': form }
    return render(request,'core/form.html', context)
