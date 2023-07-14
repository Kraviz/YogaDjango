from django.shortcuts import render, redirect, reverse
from crud.forms import ProductForm
from crud.models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from .forms import *



# Create your views here.
def index(request):
    return render(request, 'core/index.html')



def superuser_only_view(request):
    # Tu lógica de vista aquí
    return render(request, 'your_template.html')


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
                img = img,
                descripcion = descripcion
            )
            nuevo_prod.save()
            return redirect(reverse('tienda') + '?creado')
        else:
            print(form.errors)
            return redirect(reverse('tienda') + '?error')
    else:    
        form = ProductForm()
        context = {'form': form }
        context['messages'] = messages.get_messages(request)

    return render(request,'core/form.html', context)



def prod_edit(request,producto_id):
    try:
        producto = Producto.objects.get(id = producto_id)
        form = ProductForm(instance=producto)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('tienda') + '?UPDATED')
            else:
                return redirect(reverse('producto-edit', args=[producto_id]))

        context = {'form':form}
        return render(request,'core/edit.html',context)
    except:
        print("Error al obtener el producto")
        return redirect(reverse('tienda') + '?NO_EXIST')


def prod_delete(request,producto_id):
    try:
        producto = Producto.objects.get(id = producto_id)
        producto.delete()
        return redirect(reverse('tienda') + '?DELETED')
    except:
        return redirect(reverse('tienda') + '?FAIL')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'core/register.html', context)

def login(request):
    return render(request, 'core/login.html')

def create_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            telefono = form.cleaned_data.get('telefono')
            correo = form.cleaned_data.get('correo')
            asunto = form.cleaned_data.get('asunto')
            comentarios = form.cleaned_data.get('comentarios')
            nuevo_contacto = Contacto.objects.create(
                user = user,
                nombre = nombre,
                apellido = apellido,
                telefono = telefono,
                correo = correo,
                asunto = asunto,
                comentarios = comentarios
            )
            nuevo_contacto.save()
            return redirect(reverse('contacto') + '?creado')
        else:
            print(form.errors)
            return redirect(reverse('contacto') + '?error')
    else:    
        form = ContactoForm()
        context = {'form': form }
        

    return render(request,'core/contacto.html', context)


