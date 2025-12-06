from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        Post.objects.create(titulo=titulo, conteudo=conteudo)
        return redirect('post_list')
    return render(request, 'posts/create.html')

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.save()
        return redirect('post_detail', id=post.id)
    return render(request, 'posts/edit.html', {'post': post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/delete.html', {'post': post})
