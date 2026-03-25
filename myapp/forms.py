from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile, Product, ProductRequest


DEPARTMENT_CHOICES = [
    ('cse', 'Computer Science Engineering'),
    ('ece', 'Electronics & Communication Engineering'),
    ('eee', 'Electrical & Electronics Engineering'),
    ('mech', 'Mechanical Engineering'),
    ('civil', 'Civil Engineering'),
    ('it', 'Information Technology'),
    ('aiml', 'Artificial Intelligence & Machine Learning'),
    ('other', 'Other'),
]

YEAR_CHOICES = [
    (1, '1st Year'),
    (2, '2nd Year'),
    (3, '3rd Year'),
    (4, '4th Year'),
]


def validate_srit_email(value):
    if not value.endswith('@sritcbe.ac.in'):
        raise ValidationError('Only SRIT college email addresses (@sritcbe.ac.in) are allowed to register.')


class UserProfileForm(forms.ModelForm):
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    current_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'college_name',
            'department',
            'current_year',
            'graduation_year',
            'favorite_food'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Year'}),
            'favorite_food': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Favorite Food'}),
        }


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        required=True,
        validators=[validate_srit_email],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'yourname@sritcbe.ac.in'})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    current_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    graduation_year = forms.IntegerField(
        min_value=2020,
        max_value=2030,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Year'})
    )
    favorite_food = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Favorite Food (Security Question)'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'department',
            'current_year',
            'graduation_year',
            'favorite_food'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@sritcbe.ac.in'):
            raise ValidationError('Email must be from SRIT College (@sritcbe.ac.in)')

        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered.')

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                college_name='SRIT',
                department=self.cleaned_data['department'],
                current_year=int(self.cleaned_data['current_year']),
                graduation_year=self.cleaned_data['graduation_year'],
                favorite_food=self.cleaned_data['favorite_food']
            )
        return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'condition', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your product'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'id_image'}),
        }

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Message to seller (optional)'}),
        }