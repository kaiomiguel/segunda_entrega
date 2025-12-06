from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment, Category

# -------------------- POSTS --------------------

def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comentarios = post.comentarios.all()
    return render(request, 'posts/detail.html', {
        'post': post,
        'comentarios': comentarios,
    })

@login_required
def post_create(request):
    categorias = Category.objects.all()  # para passar pro template
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        post = Post.objects.create(titulo=titulo, conteudo=conteudo)

        # capturar categorias selecionadas
        categorias_selecionadas = request.POST.getlist('categorias')
        if categorias_selecionadas:
            post.categorias.set(categorias_selecionadas)

        return redirect('post_list')
    return render(request, 'posts/create.html', {'categorias': categorias})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    categorias = Category.objects.all()
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.save()

        categorias_selecionadas = request.POST.getlist('categorias')
        if categorias_selecionadas:
            post.categorias.set(categorias_selecionadas)

        return redirect('post_detail', id=post.id)
    return render(request, 'posts/edit.html', {'post': post, 'categorias': categorias})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/delete.html', {'post': post})


def category_list(request):
    categorias = Category.objects.all()
    return render(request, 'posts/category_list.html', {'categorias': categorias})

def category_detail(request, id):
    categoria = get_object_or_404(Category, id=id)
    posts = categoria.posts.all().order_by('-data_postagem')
    return render(request, 'posts/category_detail.html', {
        'posts': posts,
        'categoria': categoria
    })

@login_required
def category_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if nome:
            Category.objects.create(nome=nome, descricao=descricao)
            return redirect('category_list')
    return render(request, 'posts/category_create.html')


@login_required
def comment_create(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        conteudo = request.POST.get("texto")
        nome_autor = request.user.username
        email = request.user.email
        Comment.objects.create(
            post=post,
            nome_autor=nome_autor,
            email=email,
            conteudo=conteudo,
            data_criacao=timezone.now(),
            aprovado=True
        )
        return redirect('post_detail', id=post.id)
    return render(request, 'posts/comment_create.html', {'post': post})
