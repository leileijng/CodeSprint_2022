from django import forms

from Homepage.models import JobListing, Individual, Company, CoLoadingListing


class LoginForm(forms.Form):
    USERORCOMPANY = [ ('1','KD Tenant'), ('2','Third Party'),]
    Choice = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=USERORCOMPANY)
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class UserSignupForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True)
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),required=True)
    Resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Individual
        fields = '__all__'

class CompanySignupForm(forms.ModelForm):
    CompanyName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    UEN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Industry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    Documents = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Company
        fields = '__all__'

class PostJobs(forms.ModelForm):
    JobTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Salary = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Source = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    JobDescription = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = JobListing
        fields = '__all__'
        # exclude = ['Company', 'Source']

class PostCoLoadingListing(forms.ModelForm):
    Date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Destination = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    AvailableVolume = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    AvailableWeight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    RequiredVolume = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    RequiredWeight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)

    class Meta:
        model = CoLoadingListing
        fields = '__all__'

class Verification(forms.Form):
    VerificationCode = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class ServicesRequest(forms.ModelForm):
    VerificationCode = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
