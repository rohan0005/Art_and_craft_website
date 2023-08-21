from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
#Login required
from django.contrib.auth.decorators import login_required
# Paginator
from django.core.paginator import Paginator
from math import ceil


# Create your views here.


def index(request):
    return render(request, "index.html")


# Explore Page
def explore(request, category=None):
    
    Items = UserUploadedItem.objects.all().order_by('-id')
    
    # Pagination   
    paginator = Paginator(Items,6)
    pageNum = request.GET.get('page') 
    # current page
    allItems = paginator.get_page(pageNum)
    
    # Total Page
    totalPage = allItems.paginator.num_pages
    
    num_visible_pages = 3
    middle_page = int(ceil(num_visible_pages / 2))
    start_page = max(1, allItems.number - middle_page + 1)
    end_page = min(start_page + num_visible_pages, totalPage + 1)

    # Generate the list of visible pages
    page_list = range(start_page, end_page)

    cat = None
    if category:
        cat = category
        
        # is user select category
        if UserUploadedItem.objects.filter(category=category).exists():
            
            allItems = UserUploadedItem.objects.filter(category=category).order_by('-id')
            
            # is user search from category 
            if request.method=="GET":
                src = request.GET.get('search_content')
                # if search input not none
                if src != None:
                    Items = allItems.filter(title__icontains=src)
                    paginator = Paginator(Items,6)
                    pageNum = request.GET.get('page')
                    allItems = paginator.get_page(pageNum)
                    
                    # Total Page
                    totalPage = allItems.paginator.num_pages
                    
                    num_visible_pages = 3
                    middle_page = int(ceil(num_visible_pages / 2))
                    start_page = max(1, allItems.number - middle_page + 1)
                    end_page = min(start_page + num_visible_pages, totalPage + 1)

                    # Generate the list of visible pages
                    page_list = range(start_page, end_page)
                 
            else:
            
                allItems = UserUploadedItem.objects.filter(category=category).order_by('-id')
                     
        else:
            return redirect('explore')


   
    else:
        # current page
        allItems = paginator.get_page(pageNum)
        
        # Total Page
        totalPage = allItems.paginator.num_pages

        # list of pages
        page_list = range(start_page, end_page)

        # IF USER SEARCH
        if request.method=="GET":
            src = request.GET.get('search_content')

        if src != None:
            
            if UserUploadedItem.objects.filter(title__icontains=src).exists():
                allItems = UserUploadedItem.objects.filter(title__icontains=src)
            else:
                allItems = UserUploadedItem.objects.all().order_by('-id')
                  

        else:
            # PAGINATION
            # current page
            allItems = paginator.get_page(pageNum)
            
            # Total Page
            totalPage = allItems.paginator.num_pages

            # list of pages
            page_list = range(start_page, end_page)
            

    context= {
        'allItems': allItems,   
        'cat': cat,
        # paginator
        
        # Last Page
        'lastPage': totalPage,

        # Page List
        'page_list': page_list,
        
        
    }
    
    return render(request, 'explore.html', context) 


# LOGIN
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
            
            
        if user is not None:
            login(request, user)
             
            return redirect('/')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


# REGISTER
def registerUser(request):
    form = CreateUserForm()
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')

           
            messages.success(request,"Account Created for " + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


# LOGOUT
def logoutUser(request):
    
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):
    form = UserUploadedItemForm()
    
    if request.user.is_authenticated:
        first_name = request.user.first_name
    
    # filtering only items that is uploaded by current logged in user
    AllItems = UserUploadedItem.objects.filter(user=request.user).order_by('-id')
    
    #counting the total items
    total_items = UserUploadedItem.objects.filter(user=request.user).count()
           
    context = {
        'form': form,
        'AllItems' : AllItems,
        'total_items' : total_items,
        'first_name': first_name,
    }  

    return render(request, 'dashboard.html', context)

#Login is required for adding item
@login_required(login_url="login")
def addItem(request):
    form = UserUploadedItemForm()

    if request.method == 'POST':
        form = UserUploadedItemForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) #commit=False helps to not to save the form
            instance.user = request.user
            instance.save()
            # Creating a new empty form instance
            #form = UserUploadedItemForm() 
            messages.success(request,"Successfully added new item")
         
            return redirect('addItem')
        else:
                return render(request, 'dashboard.html')
           
    context = {
        'form': form,
        
    }
      
    return render(request, 'addItem.html', context)
    

#deleting item
@login_required(login_url="login")
def deleteItem(request, item_id):
    
    item = get_object_or_404(UserUploadedItem, id=item_id, user=request.user)
    item.delete()
    return redirect('dashboard')


#Edit item
def editItem(request, item_id):
    
     # If user click edit option
    
    editItem = get_object_or_404(UserUploadedItem, id=item_id, user=request.user)

    if request.method == 'POST':
        form = UserUploadedItemForm(request.POST, request.FILES, instance=editItem)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return redirect('dashboard')

    #if not a POST request or if form is not valid
    else:
        form = UserUploadedItemForm()

    
    return render(request, 'addItem.html', {'editItem':editItem, 'form': form})
