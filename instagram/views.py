from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    function to return the homepage of the application
    '''
    pic = Image.objects.all()
    return render(request,'index.html',{'pic': pic})

def image(request,pic_id):
    '''
    function that returns pages to store individual images
    '''
    pic = Image.get_image(id=pic_id)
    return render(request,'image.html',{'item': pic})

def profile(request,iden):
    '''
    function that returns individual profiles
    '''
    person = Profile.get_profile(identity=iden)
    posts = Image.get_post(jina=iden)
    return render(request,'profile.html',{'human':person,'posts':posts})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = current_user
            profile.save()
        return redirect('home')

    else:
        form = EditProfileForm()

    return render(request,'new_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def comment(request,id):
    current_user = request.user
    image = Image.get_image(id=id)
    item = get_object_or_404(Image, pk= id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_by = current_user
            comment.post = item
            comment.save()
        return redirect('home')

    else:
        form = NewCommentForm()

    return render(request,'new_comment.html',{"form": form,"images":image})

@login_required(login_url='/accounts/login/')
def post(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()

    return render(request, 'new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search(request):
    '''
    function that returns the search page and the searched items
    '''
    if 'name' in request.GET and request.GET['name']:
        jina = request.GET.get('name')
        profile = Profile.search_profile(jina)

        title = 'Search'
        return render(request,'search.html',{'title':title, 'content': profile})

    else:
        return render(request,'search.html')

@login_required(login_url="/accounts/login/")
def like(request,operation,pk):
   image = get_object_or_404(Image,pk=pk)
   if operation == 'like':
       image.likes.likes += 1
       image.save()
       return redirect('home')
