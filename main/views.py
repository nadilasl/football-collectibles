from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Football Collectibles',
        'name': 'Nadila Salsabila Fauziyyah',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)