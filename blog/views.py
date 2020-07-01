from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post,Skill,Education,Work
from .forms import PostForm,edForm,workForm

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})


def cv_view(request):
    if request.method=="POST":
        Skill.objects.create(text=request.POST['skill_text'])
        return redirect('/cv/')
    skills=Skill.objects.all()
    eds=Education.objects.all()
    works=Work.objects.all()
    return render (request,'blog/cv_view.html',{'skills':skills,'eds':eds,'works':works})


def cv_education(request):
    if request.method=="POST":
        form=edForm(request.POST)
        if form.is_valid():
            ed=form.save(commit=False)
            ed.save()
            return redirect('cv_view')
    else:
        ed_form=edForm()
    return render (request,'blog/cv_education.html',{'ed_form':ed_form})

def cv_education_edit(request,pk):
    ed=get_object_or_404(Education,pk=pk)
    if request.method=="POST":
        form=edForm(request.POST, instance=ed)
        if form.is_valid():
            ed=form.save(commit=False)
            ed.save()
            return redirect('cv_view')
    else:
        ed_form=edForm(instance=ed)
    return render (request,'blog/cv_education.html',{'ed_form':ed_form})


def cv_work(request):
    if request.method=="POST":
        form=workForm(request.POST)
        if form.is_valid():
            work=form.save(commit=False)
            work.save()
            return redirect('cv_view')
    else:
        work_form=workForm()
    return render (request,'blog/cv_work.html',{'work_form':work_form})

def cv_work_edit(request,pk):
    work=get_object_or_404(Work,pk=pk)
    if request.method=="POST":
        form=workForm(request.POST, instance=work)
        if form.is_valid():
            work=form.save(commit=False)
            work.save()
            return redirect('cv_view')
    else:
        work_form=workForm(instance=work)
    return render (request,'blog/cv_work.html',{'work_form':work_form})