from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Employee
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    
    context = {
        'nama_aplikasi' : 'Football Collectibles',
        'name': 'Nadila Salsabila Fauziyyah',
        'class': 'PBP E',
        'product_list': product_list # mengambil seluruh objek Produk yg tersimapn pd database
    }

    return render(request, "main.html", context)

# add employee, bebas sesuai user input
def add_employee(request):
    new_employee = Employee.objects.create(
        name = "Nadila",
        age = 20,
        persona = "Mahasiswaaaaaaaa"
    )
    
    return HttpResponse(200)

def show_employee(request):
    employee = Employee.objects.all()
    context = {
        "employees" : employee,
    }
    
    return render(request, "add_employee.html", context)

# menghasilkan form yg dapat menambahkan data Product secara otomatis ketika data di submit dari form
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

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
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
            return HttpResponse(status=404)