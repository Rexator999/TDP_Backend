from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Client, Seller, ClientRequest, SellerProduct
from .forms import SellerForm

ClientAccess = 0
SellerAccess = 0

ClientLoginEmail = ''
SellerLoginEmail = ''

def landingpage(request):
    return render(request, 'website/landingpage.html')

def clientloginpage(request):
    global ClientAccess
    global ClientLoginEmail
    if request.method == 'POST':
        UserEmail = request.POST['email']
        UserPassword = request.POST['password']
        if not UserEmail or not UserPassword:
            return render(request, 'website/sellerlogin.html', {'error_message': 'Please enter your email and Password'})
        try:
            user = Client.objects.get(email=UserEmail, password=UserPassword)
            ClientAccess = 1
            ClientLoginEmail = UserEmail
            return redirect("client1")
        except Client.DoesNotExist:
            Access = 0
            return render(request, 'website/clientlogin.html', {'error_message': 'Email and Password Invalid'})
    return render(request, 'website/clientlogin.html')

def clientregisterpage(request):
    if request.method == 'POST':
        registeredemail = request.POST.get('email')
        registeredpassword = request.POST.get('password')        
        
        client_registration = Client(
            email=registeredemail,
            password=registeredpassword,
        )
        client_registration.save()
        return render(request, 'website/clientlogin.html')
    return render(request, 'website/clientregister.html')   


def clientpage1(request):
    global ClientAccess
    if ClientAccess == 1:
        if request.method == 'POST':
            key_words = request.POST.getlist('keywords')
            
            context = {
                'key_words' : key_words,
            }
            return render(request, 'website/client2.html', context)
        return render(request, 'website/client1.html')
    else:
        return render(request, 'website/landingpage.html')

def clientpage2(request):
    global ClientAccess
    global ClientLoginEmail
    if ClientAccess == 1:
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
                client=ClientLoginEmail,
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
                'client': ClientLoginEmail,
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
    else:
        return render(request, 'website/landingpage.html')
    
def sellerloginpage(request):
    global SellerAccess
    global SellerLoginEmail
    if request.method == 'POST':
        UserEmail = request.POST['email']
        UserPassword = request.POST['password']
        if not UserEmail or not UserPassword:
            return render(request, 'website/sellerlogin.html', {'error_message': 'Please enter your email and Password'})
        try:
            user = Seller.objects.get(email=UserEmail, password=UserPassword)
            SellerAccess = 1
            SellerLoginEmail = UserEmail
            return redirect("seller")
        except Seller.DoesNotExist:
            Access = 0
            return render(request, 'website/sellerlogin.html', {'error_message': 'Email and Password Invalid'})
    return render(request, 'website/sellerlogin.html')

def sellerregisterpage(request):
    if request.method == 'POST':
        registeredemail = request.POST.get('email')
        registeredpassword = request.POST.get('password')        
        
        seller_registration = Seller(
            email=registeredemail,
            password=registeredpassword,
        )
        seller_registration.save()
        return render(request, 'website/sellerlogin.html')
    return render(request, 'website/sellerregister.html')   



def sellerpage(request):
    global SellerAccess
    if SellerAccess == 1:
        if request.method == 'POST':
            form = SellerForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save()
                return redirect('imagesuccess', image_id=instance.id)
        else:
            form = SellerForm()
        return render(request, 'website/seller.html', {'form': form})
    else:
        return render(request, 'website/landingpage.html')

def imagesuccess(request, image_id):
    global SellerAccess
    if SellerAccess == 1:
        image = SellerProduct.objects.get(id=image_id)
        return render(request, 'website/successimage.html', {'image': image})
    else:
        return render(request, 'website/landingpage.html')
