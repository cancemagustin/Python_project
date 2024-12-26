from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, DeleteView
# Create your views here.



def actualizar_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = PostForm(instance=post)
    return render(request, 'app_libros/post_update.html', context={"form": form, "post": post})



class PostListView(ListView):
    model = Post
    template_name = "app_libros/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset


class PostDetailView(DetailView):
    model = Post



"""

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


"""
def eliminar(request,pk):
    post = get_object_or_404(Post, id=pk)
    if request.method=="POST":
        post.delete()
        return redirect("blog:post_list")
    contexto = {"post":post}
    return render(request, 'app_libros/post_confirm_delete.html', contexto)



def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect("blog:post_list")
            else:
                form.add_error(None, "Debes estar logueado para crear una publicación. ")
    else:
        form = PostForm()
    return render(request, "app_libros/post_create.html", context={"form": form})