from django.shortcuts import render
from django.utils import timezone
from .models import Post, WorkElement, EduElement, Skills, Extra
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, WorkForm, EduForm, SkillsForm, ExtraForm
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




def work_edit(request, pk):

    work = get_object_or_404(WorkElement, pk=pk)
    if request.method == "POST":
     
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            work.author = request.user
            work.published_date = timezone.now()
            work.save()
            return redirect('/')
    else:
        form = WorkForm(instance=work)
    return render(request, 'blog/field_edit.html', {'form': form})


def edu_edit(request, pk):

    edu = get_object_or_404(EduElement, pk=pk)
    if request.method == "POST":
     
    
        form = EduForm(request.POST, instance=edu)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.published_date = timezone.now()
            edu.save()
            return redirect('/')
    else:
        form = EduForm(instance=edu)
    return render(request, 'blog/field_edit.html', {'form': form})


def skills_edit(request, pk):

    skill = get_object_or_404(Skills, pk=pk)
    if request.method == "POST":
    
        form = SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.author = request.user
            skill.published_date = timezone.now()
            skill.save()
            return redirect('/')
    else:
        form = SkillsForm(instance=skill)
    return render(request, 'blog/field_edit.html', {'form': form})


def extra_edit(request, pk):

    extra = get_object_or_404(Extra, pk=pk)
    if request.method == "POST":

        form = ExtraForm(request.POST, instance=extra)
        if form.is_valid():
            extra = form.save(commit=False)
            extra.author = request.user
            extra.published_date = timezone.now()
            extra.save()
            return redirect('/')
    else:
        form = ExtraForm(instance=extra)
    return render(request, 'blog/field_edit.html', {'form': form})