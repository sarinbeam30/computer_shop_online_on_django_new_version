from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, get_user_model

class Register_Form(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    username = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(help_text='Minimum length of this field must be equal or greater than 6 symbols. Leading and trailing spaces will be ignored.'
            , required='True' ,widget=forms.TextInput(attrs={'type' : 'password'}))
    password2 = forms.CharField(help_text='', required=True, widget=forms.TextInput(attrs={'type' : 'password'}))

    #mobile_numberfield
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    mobile_number = forms.CharField(validators=[phone_regex], max_length=10, required=True) # validators should be a list

    #edit_label_on_html
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email"
        self.fields['mobile_number'].label = "Mobile Number"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm password"


    class Meta :
        model = User
        fields = ('first_name','last_name','username', 'email', 'mobile_number', 'password1', 'password2', )



class Login_Form(AuthenticationForm):
    
    username = forms.CharField(max_length=60, required=True)
    password = forms.CharField(help_text='', required=True, max_length=60 ,widget=forms.TextInput(attrs={'type' : 'password'}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        kwargs.setdefault('label_suffix', '')
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        self.fields['username'].label = "Email or Username"
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
        return self.cleaned_data
    
    def check_for_test_cookie(self):
        warnings.warn("check_for_test_cookie is deprecated; ensure your login "
                "view is CSRF-protected.", DeprecationWarning)

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


#CART-FUNCTION
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)