from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ClientRequest, Seller
from .forms import SellerForm

def homepage(request):
    return render(request, 'website/home.html')

def clientpage1(request):
    if request.method == 'POST':
        key_words = request.POST.getlist('keywords')
        
        context = {
            'key_words' : key_words,
        }
        return render(request, 'website/client2.html', context)
    return render(request, 'website/client1.html')

def clientpage2(request):
    if request.method == 'POST':
        min_price = request.POST.get('minPrice')
        max_price = request.POST.get('maxPrice')
        current_date = request.POST.get('currentdate')
        product_type = request.POST.get('productType')
        product_details = request.POST.get('productdetails')
        key_words = request.POST.getlist('keywords')
        most_views = bool(request.POST.get('MostViews', False))
        newest = bool(request.POST.get('Newest', False))
        top_rated = bool(request.POST.get('TopRated', False))

        #This is used to save to database
        client_request = ClientRequest(
            min_price=min_price,
            max_price=max_price,
            current_date=current_date,
            product_type=product_type,
            product_details=product_details,
            key_words=','.join(key_words),
            most_views=most_views,
            newest=newest,
            top_rated=top_rated,
        )
        client_request.save()
        
        context = {
            'min_price': min_price,
            'max_price': max_price,
            'current_date': current_date,
            'product_type': product_type,
            'product_details': product_details,
            'key_words' : key_words,
            'most_views': most_views,
            'newest': newest,
            'top_rated': top_rated,
        }
        return render(request, 'website/clientresults.html', context)
    return render(request, 'website/client2.html')

def sellerpage(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('imagesuccess', image_id=instance.id)
    else:
        form = SellerForm()
    return render(request, 'website/seller.html', {'form': form})

def imagesuccess(request, image_id):
    image = Seller.objects.get(id=image_id)
    return render(request, 'website/successimage.html', {'image': image})

def testingpage(request):
    return render(request, 'website/test.html')
