from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class SignUpForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already Taken')
        return username

    def clean(self):
        """verifies password confirmation"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data

    def save(self):
        """create user in database"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        max_length=254,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        exclude = ('user',)
        widgets = {
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            user = instance.user
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self):
        data = self.cleaned_data
        profile = self.instance

        profile.user.first_name = data.get('first_name')
        profile.user.last_name = data.get('last_name')
        profile.user.email = data.get('email')
        profile.user.save()
        return super().save()
