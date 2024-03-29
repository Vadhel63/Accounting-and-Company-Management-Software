from django import forms
from django.contrib.auth.models import User
from Inventory.models import StaffProfile

class StaffProfileForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    POSITION_CHOICES = [
        ('HR_Manager', 'HR Manager'),
        ('Accountant_Manager', 'Accountant Manager'),
        ('Inventory_Manager', 'Inventory Manager'),
        ('Admin', 'Admin'),
    ]

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    position = forms.ChoiceField(choices=POSITION_CHOICES)

    class Meta:
        model = StaffProfile
        fields = ['name', 'position', 'email', 'gender', 'phone_number', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(StaffProfileForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget = forms.Select(choices=self.GENDER_CHOICES)
        self.fields['position'].widget = forms.Select(choices=self.POSITION_CHOICES)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise forms.ValidationError('Mobile number must be a 10-digit number.')
        return mobile_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please enter them again.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        staff_profile = super(StaffProfileForm, self).save(commit=False)
        staff_profile.user = user
        if commit:
            staff_profile.save()
        return staff_profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
