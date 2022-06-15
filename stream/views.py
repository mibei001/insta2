from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from stream.forms import PostForm, RegistrationForm, UpdateProfileForm, UpdateUserForm, CommentForm, UpdatePostForm
from django.contrib.auth.models import User
from stream.models import Comment, Post, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.


def home_page(request):
    # have to use timed because time is already inbuilt
    post = Post.objects.all().order_by("-timed_created")

    context = {
        "posts": post,
    }

    return render(request, 'all-posts/home_page.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()

            for user in User.objects.all():
                # get_or_create returns the object that it got and a boolean value that specifies whether the object was created or not.

                # basically get_or_create is for avoiding duplicates

                # cleaned_data returns a dic of validated form input fields and their values
                username = registerForm.cleaned_data.get('username')
                messages.success(
                    request, f'An account has been created for {username}')
                return redirect('login')

    else:
        registerForm = RegistrationForm()

    return render(request, 'registration/register.html', {"form": registerForm})

# post_save - signals works after a model's save() method is called.
# receiver - the function who receives the signals and does something
# sender - sends the signal
# created - checks whether the model is created or not
# instance - created model instance
# kwargs - wildcard keyword arguments
# >>>> link to the source >>>> https://medium.com/analytics-vidhya/signals-in-django-af99dabeb875  <<<<


# we are using receiver decorator to call the create_user_profile function on creation of user instance.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@login_required
@csrf_protect
def profile(request):
    if request.method == "POST":
        mtumiaji = UpdateUserForm(request.POST, instance=request.user)
        profile = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if mtumiaji.is_valid() and profile.is_valid():
            mtumiaji.save()
            profile.save()
            messages.success(
                request, f'The account has been updated successfully')
            return redirect('profile')

    else:
        mtumiaji = UpdateUserForm(instance=request.user)
        profile = UpdateProfileForm(instance=request.user.profile)

    user_post = Post.objects.filter(
        mtumiaji=request.user).order_by("-timed_created")
    post = Post.objects.filter(
        mtumiaji=request.user).order_by("-timed_created")

    context = {
        "user_form": mtumiaji,
        "profile_form": profile,
        "user_post": user_post,
        "posts": post,
    }
    return render(request, 'registration/profile.html', context)


@login_required
def new_post(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                image=form.cleaned_data["image"],
                image_name=form.cleaned_data["image_name"],
                image_caption=form.cleaned_data["image_caption"],
                mtumiaji=request.user
            )
            post.save()
            print(post)
            name_of_post = form.cleaned_data.get("image_name")
            messages.success(request, f'Post has been created {name_of_post}')
            return redirect('home_page')

    else:
        form = PostForm()

    return render(request, 'all-posts/new_post.html', {"form": form})


@login_required
@csrf_protect
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    mtumiaji = request.user
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=mtumiaji, body=form.cleaned_data['body'], post=post)

            comment.save()

    comments = Comment.objects.filter(post=post).order_by("-time_created")
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "all-posts/post_detail.html", context)


@login_required
def like(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes += 1
    post.save()

    return redirect("home_page")


@login_required
def delete_post(request, id):
    kitu = Post.objects.get(id=id)
    kitu.delete()
    return redirect("home_page")


@login_required
def edit_post(request, id):
    edit = Post.objects.get(pk=id)
    form = UpdatePostForm(request.POST or None,
                          request.FILES or None, instance=edit)
    if form.is_valid():
        form.save()
        return redirect('home_page')

    return render(request, 'all-posts/edit_post.html',
                  {"form": form,
                   "edit": edit})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(
            image_name__contains=searched)

        return render(request,
                      'all-posts/search_venues.html',
                      {'searched': searched,
                       'posts': posts})

    else:
        return render(request,
                      'all-posts/search_venues.html',
                      {})
