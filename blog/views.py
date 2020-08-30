from django.shortcuts import render
from django.utils import timezone
from .models import Post, WorkElement, EduElement, Skills, Extra
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
   posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   jobs = WorkElement.objects.filter(published_date__lte=timezone.now()).order_by('-dates')  
   edu = EduElement.objects.filter(published_date__lte=timezone.now()).order_by('dates')
   skills = Skills.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
   extra = Extra.objects.filter(published_date__lte=timezone.now()).order_by('created_date')

   return render(request, 'blog/post_list.html', {'posts': posts, 'jobs': jobs, 'edu':edu,'skills':skills,'extra':extra})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Post.objects.get(pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):#passing in extra param
    #get post model we want to edit

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        #when we want to create a form - pass this post as an instance
    
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})