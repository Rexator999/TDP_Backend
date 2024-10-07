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
            return render(request, 'website/clientpreferences.html', context)
        return render(request, 'website/clientkeywords.html')
    else:
        return render(request, 'website/landingpage.html')
    
def clientpage1_2(request):
    global ClientAccess
    if ClientAccess == 1:
        if request.method == 'POST':
            key_words = request.POST.getlist('keywords')
            
            context = {
                'key_words' : key_words,
            }
            return render(request, 'website/clientpreferences.html', context)
        return render(request, 'website/clientkeywords2.html')
    else:
        return render(request, 'website/landingpage.html')

def clientpage2(request):
    global ClientAccess
    global ClientLoginEmail
    if ClientAccess == 1:
        if request.method == 'POST':
            min_price = request.POST.get('minPrice')
            max_price = request.POST.get('maxPrice')
            date_selection = request.POST.get('date')
            current_date = request.POST.get('currentdate')
            product_type = request.POST.get('productType')
            product_details = request.POST.get('productdetails')
            key_words = request.POST.getlist('keywords')
            firstHand = bool(request.POST.get('MostViews', False))
            secondHand = bool(request.POST.get('Newest', False))

            if date_selection == 'Custom':
                date_selection = current_date,

            #This is used to save to database
            client_request = ClientRequest(
                client=ClientLoginEmail,
                min_price=min_price,
                max_price=max_price,
                end_date=date_selection,
                product_type=product_type,
                product_details=product_details,
                key_words=','.join(key_words),
                firsthand=firstHand,
                secondhand=secondHand,
            )
            client_request.save()
                
            context = {
                'client': ClientLoginEmail,
                'min_price': min_price,
                'max_price': max_price,
                'current_date': current_date,
                'end_date': date_selection,
                'product_type': product_type,
                'product_details': product_details,
                'key_words' : key_words,
                'firsthand': firstHand,
                'secondhand': secondHand,
            }
            return render(request, 'website/clientresults.html', context)
        return render(request, 'website/clientpreferences.html')
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
            return redirect("seller1")
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

def sellerpage1(request):
    global SellerAccess
    if SellerAccess == 1:
        if request.method == 'POST':
            key_words = request.POST.getlist('keywords')
            
            context = {
                'key_words' : key_words,
            }
            return render(request, 'website/sellerimage.html', context)
        return render(request, 'website/sellerkeywords.html')
    else:
        return render(request, 'website/landingpage.html')
    
def sellerpage1_2(request):
    global SellerAccess
    if SellerAccess == 1:
        if request.method == 'POST':
            key_words = request.POST.getlist('keywords')
            
            context = {
                'key_words' : key_words,
            }
            return render(request, 'website/sellerimage.html', context)
        return render(request, 'website/sellerkeywords2.html')
    else:
        return render(request, 'website/landingpage.html')

def sellerpage2(request):
    global SellerAccess
    if SellerAccess == 1:
        if request.method == 'POST':
            image = request.FILES.get('image')
            key_words = request.POST.getlist('keywords')

            seller_product = SellerProduct(
                seller=SellerLoginEmail,
                image=image,
                key_words=','.join(key_words),
            )
            seller_product.save()

            context = {
                'seller' : SellerLoginEmail,
                'image' : seller_product.image.url,
                'key_words' : key_words,
            }
            return render(request, 'website/sellerproduct.html', context)
        return render(request, 'website/sellerimage.html')
    else:
        return render(request, 'website/landingpage.html')
