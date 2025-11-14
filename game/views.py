from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.decorators.http import require_POST
from .models import Operator,Post, Reply, Like
from django.urls import reverse_lazy, reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Post, Reply, Weapon
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReplyForm
from django.views.generic.edit import FormMixin
from django.db.models import Q  # for complex lookups
# Create your views here.

class OperatorList(ListView):
    model = Operator
    template_name = "game/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(skin__icontains=query) | Q(faction__icontains=query)
            )
        return queryset


class OperatorDetail(DetailView):
    model = Operator
    template_name = "game/details.html"

class WeaponList(ListView):
    model = Weapon
    template_name = "game/weaponlist.html"
    context_object_name = 'weapon_list'  

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset
class WeaponDetail(DetailView):
    model = Weapon
    template_name = "game/weapondetail.html"

@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    
    if request.user == reply.author or request.user.is_staff:
        post_id = reply.post.id
        reply.delete()
        messages.success(request, "Your reply was deleted successfully.")
        return redirect('post_list')  
    else:
        messages.error(request, "You do not have permission to delete this reply.")
        return redirect('post_detail', pk=reply.post.id)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'forum/post_confirm_delete.html'  
    success_url = reverse_lazy('post_list')    

    def get_queryset(self):       
       return super().get_queryset().filter(author=self.request.user)



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']  
    template_name = 'game/post.html'
    success_url = reverse_lazy('post_list')

    ## before save, set the logged in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    try:
        Like.objects.create(user=request.user, post=post)
        post.likes += 1
        post.save()
    except IntegrityError:
       print("IntegrityError")
       print(IntegrityError)
       pass

    return redirect('post_list')

class PostList(ListView):
    model = Post
    template_name = "game/forum.html"
    context_object_name = 'post_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

class PostDetail(DetailView):
    model = Post
    template_name = "game/forum.html"
    form_class = ReplyForm

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        replies = Reply.objects.filter(post=post).order_by('created_at')  # or your timestamp field
        context = {
            'post': post,
            'replies': replies,
        }
        return render(request, 'game/post_detail.html', context)

    def get_success_url(self):
        return self.request.path  # reload the same page


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # get the Post instance
        form = self.get_form()

        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = self.object
            if request.user.is_authenticated:
                reply.author = request.user
            reply.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)





class AddReply(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'game/reply_form.html'
    login_url = 'login'  
    redirect_field_name = 'next'  

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        
        return reverse('post_list')


class ReplyList(ListView):
    model = Reply
    template_name = "game/forum.html"