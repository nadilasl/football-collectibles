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
import requests
import json

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
        
        # Deteksi AJAX request
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        
        if form.is_valid():
            user = form.save()
            
            # Return JSON untuk AJAX
            if is_ajax:
                return JsonResponse({
                    'success': True,
                    'message': 'Your account has been successfully created!',
                    'redirect': reverse('main:login'),
                    'username': user.username
                }, status=201)
            
            # Non-AJAX fallback
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            # Registrasi gagal
            if is_ajax:
                errors = {
                    'non_field_errors': [],
                    'field_errors': {}
                }
                
                # Non-field errors
                if form.non_field_errors():
                    errors['non_field_errors'] = list(form.non_field_errors())
                
                # Field errors
                for field, error_list in form.errors.items():
                    if field != '__all__':
                        errors['field_errors'][field] = list(error_list)
                
                return JsonResponse({
                    'success': False,
                    **errors
                }, status=400)
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      
      # Deteksi AJAX request
      is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        # Return JSON untuk AJAX
        if is_ajax:
            return JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'redirect': reverse('main:show_main'),
                'username': user.username
            }, status=200)
        
        # Non-AJAX fallback
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        # Login gagal
        if is_ajax:
            errors = {
                'non_field_errors': [],
                'field_errors': {}
            }
            
            # Non-field errors
            if form.non_field_errors():
                errors['non_field_errors'] = list(form.non_field_errors())
            
            # Field errors
            for field, error_list in form.errors.items():
                if field != '__all__':
                    errors['field_errors'][field] = list(error_list)
            
            return JsonResponse({
                'success': False,
                **errors
            }, status=400)

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

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            # Extract data dari Flutter form (request.POST, bukan JSON)
            name = strip_tags(request.POST.get("name", ""))
            price = request.POST.get("price", "0")
            description = strip_tags(request.POST.get("description", ""))
            thumbnail = request.POST.get("thumbnail", "")
            category = request.POST.get("category", "jersey")
            stock = request.POST.get("stock", "0")
            brand = request.POST.get("brand", "")
            release_year = request.POST.get("release_year", "")
            size = request.POST.get("size", "")
            edition_type = request.POST.get("edition_type", "replica")
            condition = request.POST.get("condition", "new")
            authenticity_certificate = request.POST.get("authenticity_certificate", "false") == "true"
            rarity_level = request.POST.get("rarity_level", "common")
            is_featured = request.POST.get("is_featured", "false") == "true"
            
            # Debug print
            print("=" * 60)
            print("✅ CREATE PRODUCT REQUEST")
            print(f"Name: {name}")
            print(f"Price: {price}")
            print(f"Category: {category}")
            print(f"User: {request.user}")
            print("=" * 60)
            
            # Create Product
            new_product = Product.objects.create(
                user=request.user,
                name=name,
                price=int(price) if price else 0,
                description=description,
                thumbnail=thumbnail,
                category=category,
                stock=int(stock) if stock else 0,
                brand=brand,
                release_year=int(release_year) if release_year else None,
                size=size if size else '',
                edition_type=edition_type,
                condition=condition,
                authenticity_certificate=authenticity_certificate,
                rarity_level=rarity_level,
                is_featured=is_featured,
            )
            
            print(f"✅ Product created with ID: {new_product.id}")
            
            # Return response yang Flutter expect
            return JsonResponse({
                "status": "success",
                "message": f"Product '{name}' berhasil ditambahkan!",
                "data": {
                    "id": str(new_product.id),
                    "name": new_product.name,
                    "price": new_product.price,
                }
            }, status=201)
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            
            return JsonResponse({
                "status": "error",
                "message": f"Error: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({
            "status": "error",
            "message": "Method not allowed"
        }, status=405)
        
@csrf_exempt
def get_products_json(request):
    """Get all products as JSON for Flutter"""
    products = Product.objects.all().select_related('user')
    
    data = []
    for product in products:
        data.append({
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
            'user': {
                'username': product.user.username if product.user else 'Unknown',
                'id': product.user.id if product.user else None,
            }
        })
    
    return JsonResponse(data, safe=False)

@csrf_exempt  
def get_user_products_json(request):
    """Get current user's products as JSON for Flutter"""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authenticated'}, status=401)
        
    products = Product.objects.filter(user=request.user)
    
    data = []
    for product in products:
        data.append({
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
            'user': {
                'username': product.user.username if product.user else 'Unknown',
                'id': product.user.id if product.user else None,
            }
        })
    
    return JsonResponse(data, safe=False)