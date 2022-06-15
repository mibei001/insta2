from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms import ModelForm

from stream.models import NewPost, Profile


class RegistrationForm(UserCreationForm):
    barua = forms.EmailField()

    class Meta:
        model = User
        # primary att for the user are username,password,email,first_name and last_name
        fields = ['username', 'first_name', 'email', 'password']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']


class PostForm(forms.Form):
    image = forms.ImageField()
    image_name = forms.CharField()
    image_caption = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = NewPost
        fields = ['image']


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Add a comment"}))

    # Instead of forms.forms use ModelForm so that the instance in views can work


class UpdatePostForm(ModelForm):
    image = forms.ImageField()
    image_name = forms.CharField()
    image_caption = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = NewPost
        fields = ['image']
