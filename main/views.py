import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        'nama_aplikasi' : 'Football Collectibles',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list, # mengambil seluruh objek Produk yg tersimapn pd database
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

# menghasilkan form yg dapat menambahkan data Product secara otomatis ketika data di submit dari form
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id) #untuk ambil objek Product berdasarkan pk
    # kalo ga ketemu return halaman 404

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'release_year': product.release_year,
            'size': product.size,
            'edition_type': product.edition_type,
            'condition': product.condition,
            'authenticity_certificate': product.authenticity_certificate,
            'rarity_level': product.rarity_level,
            'user_id': product.user_id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)

        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'release_year': product.release_year,
            'size': product.size,
            'edition_type': product.edition_type,
            'edition_type_display': product.get_edition_type_display(),
            'condition': product.condition,
            'condition_display': product.get_condition_display(),
            'authenticity_certificate': product.authenticity_certificate,
            'rarity_level': product.rarity_level,
            'rarity_level_display': product.get_rarity_level_display(),
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }

        return JsonResponse(data)

    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

        
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    # Ambil dan bersihkan data dari form
    name = strip_tags(request.POST.get("name", ""))
    price = strip_tags(request.POST.get("price", ""))
    description = strip_tags(request.POST.get("description", ""))
    thumbnail = strip_tags(request.POST.get("thumbnail", ""))
    category = strip_tags(request.POST.get("category", ""))
    brand = strip_tags(request.POST.get("brand", ""))
    release_year = strip_tags(request.POST.get("release_year", ""))
    size = strip_tags(request.POST.get("size", ""))
    edition_type = strip_tags(request.POST.get("edition_type", ""))
    condition = strip_tags(request.POST.get("condition", ""))
    rarity_level = strip_tags(request.POST.get("rarity_level", ""))

    # Checkbox handling
    is_featured = request.POST.get("is_featured") == 'on'
    authenticity_certificate = request.POST.get("authenticity_certificate") == 'on'

    # User
    user = request.user

    # Konversi angka dengan validasi aman
    try:
        price = int(price) if price else 0
        stock = int(strip_tags(request.POST.get("stock", "0")))
        release_year = int(release_year) if release_year else None
    except ValueError:
        return HttpResponse(b"Invalid numeric value", status=400)

    # Simpan ke database
    new_product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        stock=stock,
        brand=brand,
        release_year=release_year,
        size=size,
        edition_type=edition_type,
        condition=condition,
        authenticity_certificate=authenticity_certificate,
        rarity_level=rarity_level,
        user=user
    )

    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    # Pastikan hanya owner yang bisa edit
    if request.user != product.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    # Bersihkan input dari form
    name = strip_tags(request.POST.get("name", product.name))
    price = strip_tags(request.POST.get("price", product.price))
    description = strip_tags(request.POST.get("description", product.description))
    thumbnail = strip_tags(request.POST.get("thumbnail", product.thumbnail))
    category = strip_tags(request.POST.get("category", product.category))
    brand = strip_tags(request.POST.get("brand", product.brand))
    release_year = strip_tags(request.POST.get("release_year", product.release_year))
    size = strip_tags(request.POST.get("size", product.size))
    edition_type = strip_tags(request.POST.get("edition_type", product.edition_type))
    condition = strip_tags(request.POST.get("condition", product.condition))
    rarity_level = strip_tags(request.POST.get("rarity_level", product.rarity_level))

    # Checkbox handling
    is_featured = request.POST.get("is_featured") == 'on'
    authenticity_certificate = request.POST.get("authenticity_certificate") == 'on'

    try:
        price = int(price)
        stock = int(strip_tags(request.POST.get("stock", product.stock)))
        release_year = int(release_year) if release_year else None
    except ValueError:
        return JsonResponse({'error': 'Invalid numeric value'}, status=400)

    # Update field
    product.name = name
    product.price = price
    product.description = description
    product.thumbnail = thumbnail
    product.category = category
    product.is_featured = is_featured
    product.stock = stock
    product.brand = brand
    product.release_year = release_year
    product.size = size
    product.edition_type = edition_type
    product.condition = condition
    product.authenticity_certificate = authenticity_certificate
    product.rarity_level = rarity_level
    product.save()

    return JsonResponse({'message': 'Product updated successfully'}, status=200)
