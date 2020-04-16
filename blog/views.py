from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import PostText, PostFile, Attachment,share
from .forms import PostFileForm,PostFileShareForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory, inlineformset_factory


# Create your views here.
def home(request):
    context = {
        'posts': PostText.objects.all()
    }
    return render(request, 'blog/home.html',context)


# def PostFile(request):
#     if request.method == 'POST':
#         form = PostFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#             return redirect('postfile-create')
#     else:
#         form = PostFileForm()
#     return render(request, 'blog/PostFile_form.html', {
#         'form': form
#     })

class PostFileCreateView(LoginRequiredMixin,CreateView):
    model = PostFile
    form_class = PostFileForm
    success_url = reverse_lazy('postfile-create')
    template_name = 'blog/PostFile_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.author = self.request.user
        files = request.FILES.getlist('file')
        if form.is_valid():
            Post = form.save(commit=False)
            Post.save()
            for f in files:
                postAttach = Attachment(post = Post, file = f)
                postAttach.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PostFileListView(ListView):
    model = PostFile
    template_name = 'blog/filehome.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    queryset = PostFile.objects.all()
    ordering = ['-date_posted']

class PostFileDetailView(DetailView):
    model = PostFile


class PostListView(ListView):
    model = PostText
    template_name = 'blog/home.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

   # def get_context_data( self, **kwargs):
    #     context = super(PostFileListView, self).get_context_data(**kwargs)
    #     context['files'] = Attachment.objects.all()
    #     return context

class PostFileUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = PostFile
    form_class = PostFileForm
    # fields  = ['title','expiration', 'content','file']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def post(self, request, *args, **kwargs):
        dfiles = Attachment.objects.filter(post = self.get_object())
        for f in dfiles:
            f.delete()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.author = self.request.user
        files = request.FILES.getlist('file')
        if form.is_valid():
            # Post = form.save(commit=False)
            # Post.save()
            for f in files:
                postAttach = Attachment(post = self.get_object() , file = f)
                postAttach.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def PostFileUpdate(request, id=None):
    instance = get_object_or_404(PostFile, id = id)
    form =  PostFileForm(request.POST or None, instance =instance)
    form.instance.author = request.user
    files = request.FILES.getlist('file')
    if form.is_valid():
        dfiles = Attachment.objects.filter(post = instance)
        for f in dfiles:
            f.delete()
        Post = form.save(commit=False)
        Post.save()
        for f in files:
            postAttach = Attachment(post = Post, file = f)
            postAttach.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title" : instance.title,
        "instance" : instance,
        "form" : form
    }    

    return render(request, "blog/PostFile_form.html", context)
        

class PostFileDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = PostFile
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            dfiles = Attachment.objects.filter(post = self.get_object())
            for f in dfiles:
                f.delete()
            return True
        return False



# def PostFileShare(request, id=None):
#     instance = get_object_or_404(PostFile, id = id)
#     if request.method == 'POST':
#         form = PostFileShareForm(request.POST)
#         if(form.is_valid()):
#             u_name = form.instance.viewer_username
#             try:
#                 user = User.objects.get(username=u_name)
#             except User.DoesNotExist:
#                 user = None
#             print(user)
#     else:
#         form = PostFileShareForm()
#     return render(request, "blog/PostFile_Share.html",{'form':form})


def PostFileShare(request, id=None):
    postfile = get_object_or_404(PostFile, id = id)
    ShareFormset = inlineformset_factory(PostFile,share, form = PostFileShareForm, extra = 1) #parent model , child model

    if request.method == 'POST':
        formset = ShareFormset(request.POST,instance = postfile) #parent
        if formset.is_valid():
            instances = formset.save(commit = False)
            for instance in instances :
                u_name = instance.viewer_username
                try:
                    user = User.objects.get(username=u_name)
                except User.DoesNotExist:
                    user = None
                if user == None:
                    pass
                else :
                    message1 = ('Shared with %(user_name)s successfully') % {'user_name': u_name}
                    messages.success(request, message1)
                    instance.viewer = user;
                    instance.save()
            for obj in formset.deleted_objects:
                u_name = obj.viewer_username
                message2 = ('Removed user %(user_name)s successfully') % {'user_name': u_name}
                messages.warning(request, message2)
                obj.delete()
            return redirect('post-share', id)
        else: 
            messages.warning(request, f'Please enter a correct username.')
            

            return redirect('post-share', id)
    formset = ShareFormset(instance = postfile)

    return render(request, 'blog/PostFile_Share.html', {'formset' : formset})



#done
class MyPostListView(ListView):
    model = PostText
    template_name = 'blog/my_home.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

#done
class PostDetailView(DetailView):
    model = PostText

#done
class PostCreateView(LoginRequiredMixin,CreateView):
    model = PostText
    fields  = ['title','expiration', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#done
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = PostText
    fields  = ['title','expiration', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#done
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = PostText
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


    