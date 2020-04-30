from django import forms
from .models import *


class Reg_Form(forms.Form):
    t_id = forms.IntegerField(
        label='Enter ID',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter Id (Numbers Only)',
                'class': 'form-control'
            }
        )
    )
    name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control'
            }
        )
    )
    email_id = forms.EmailField(
        label='Enter Email-ID',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email ID',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password',
                'class': 'form-control'
            }
        )
    )
    mobile_no = forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )
    address = forms.CharField(
        label='Enter Address',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Address',
                'class': 'form-control'
            }
        )
    )

    def clean_id(self):
        t_id = self.cleaned_data.get('t_id')
        query_set = Reg_Model.objects.filter(t_id=t_id)
        if query_set.exists():
            raise forms.ValidationError("User name is taken already.")
        return t_id

    def clean_email_id(self):
        email = self.cleaned_data.get('email_id')
        query_set = Reg_Model.objects.filter(email_id=email)
        if query_set.exists():
            raise forms.ValidationError("Email name is taken already.")
        elif not '@' in email:
            raise forms.ValidationError("Email should contain @")
        return email

    def clean_mobile(self):
        mobile_no = self.cleaned_data.get('mobile_no')
        query_set = Reg_Model.objects.filter(mobile_no=mobile_no)
        if mobile_no.exists():
            raise forms.ValidationError('Mobile Number Already Taken')
        elif len(str(mobile_no)) != 10:
            raise forms.ValidationError('Enter Valid Mobile Number')
        return mobile_no

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password :
            raise forms.ValidationError("Passwords must match.")
        elif len(password) <= 4 or len(password) >= 15:
            raise forms.ValidationError("Password length must be more then 4 chars or less then 15")
        return data



class LoginForm(forms.Form):
    email_id = forms.CharField(
        label='Enter Your Email-ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email-id'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )






# class StudentForm(forms.Form):
#     name = forms.CharField(
#         label='Enter Name',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': ' Name',
#                 'class': 'form-control'
#             }
#         )
#     )
#     email_id = forms.EmailField(
#         label='Enter Email',
#         widget=forms.EmailInput(
#             attrs={
#                 'placeholder': 'Email ID',
#                 'class': 'form-control'
#             }
#         )
#     )
#     password = forms.CharField(
#         label='Enter Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Password',
#                 'class': 'form-control'
#             }
#         )
#     )
#
#     confirm_password = forms.CharField(
#         label="confirm your Password",
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'confirm password',
#                 'class': 'form-control'
#             }
#         )
#     )
#     section = forms.IntegerField(
#         label='Enter Section',
#         widget=forms.NumberInput(
#             attrs={
#                 'placeholder': 'Section',
#                 'class': 'form-control'
#             }
#         )
#     )
#
#     def clean_id(self):
#         s_id = self.cleaned_data.get('t_id')
#         query_set = Student_Model.objects.filter(s_id=s_id)
#         if query_set.exists():
#             raise forms.ValidationError("User name is taken already.")
#         return s_id
#
#     def clean_email_id(self):
#         email_id = self.cleaned_data.get('email_id')
#         query_set = Student_Model.objects.filter(email_id=email_id)
#         if query_set.exists():
#             raise forms.ValidationError("Email name is taken already.")
#         elif not '@' in email_id:
#             raise forms.ValidationError("Email should contain @")
#         return email_id
#
#     def clean_password(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if confirm_password != password:
#             raise forms.ValidationError("Passwords must match.")
#         elif len(password) <= 4 or len(password) >= 15:
#             raise forms.ValidationError("Password length must be more than 4 chars or less than 15")
#         return data
