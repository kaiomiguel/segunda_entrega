from django.db import models
from django.utils import timezone

# Categoria do post
class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

# Post do blog
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()  # armazenará HTML
    data_postagem = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField('Category', related_name='posts', blank=True)

    def __str__(self):
        return self.titulo

# Comentário de um post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    nome_autor = models.CharField(max_length=100)
    email = models.EmailField()
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Comentário de {self.nome_autor} no post "{self.post.titulo}"'
