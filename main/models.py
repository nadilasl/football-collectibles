from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        # formatnya (value, label). Value disimpan di databse dan Label ditampilkan di form/admin
        ('jersey', 'Jersey'),
        ('scarves_banner', 'Scarves or Banners'),
        ('footballs', 'Collector Footballs'),
        ('autographed', 'Autographed Memorabilia'),
        ('second_hand', 'Second-Hand Collectible'),
        ('limited_edition', 'Limited Edition Item'),
        ('authentic_retail', 'Authentic Retail Jersey'),
        ('replica_jersey', 'Replica Jersey'),
        ('match_worn', 'Match-Worn Jersey'),
    ]
    
    name = models.CharField(max_length=100) #max_length ini akan divalidasi di form
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField() 
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0) #positive agar tidak ada nilai negatif
    brand = models.CharField(max_length=50, blank=True)
    release_year = models.IntegerField(blank=True, null=True) #blank=True artinya optional (tidak wajib diisi) dan null=True artinya boleh NULL di database
    size = models.CharField(max_length=3, choices=[
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
    ], blank=True)
    edition_type = models.CharField(max_length=20, choices=[
        ('replica', 'Replica'),
        ('limited', 'Limited Edition'),
        ('secondhand', 'Second Hand')
    ], default = 'replica')
    condition = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
    ], default ='new')
    authenticity_certificate = models.BooleanField(default=False) 
    rarity_level = models.CharField(max_length=20, choices=[
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('legendary', 'Legendary')
    ], default='common')
    
    # Method __str__ untuk mengembalikan representasi string dari objek
    def __str__(self):
        return self.name
    
    # char field untuk teks pendek
    # text field dapat menampun teks panjang
    # URLField menyimpan URL gambar yang bersifat optional
    # is_featured apakah produk ini adalah produk unggulan
    # blank artinya bisa dikonsongkan saat input
    # null boleh menyimpan NULL
    