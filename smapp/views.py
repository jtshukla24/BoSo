from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *
from .forms import *



# Start Page

def home(request):
    return render(request, 'index.html')



# User Portal

def user_signup_view(request):
    if request.method == 'POST':

        tform = Reg_Form(request.POST)

        if tform.is_valid():
            print(tform.cleaned_data)

            t_id = request.POST.get('t_id')
            name = request.POST.get('name')
            email_id = request.POST.get('email_id')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            mobile_no = request.POST.get('mobile_no')
            address = request.POST.get('address')
            data = Reg_Model(t_id=t_id, name=name, email_id=email_id, password=password,
                             address=address,confirm_password=confirm_password,
                             mobile_no=mobile_no)
            data.save()
            tform = Reg_Form()
            return render(request, 'teacher_form.html', {'tform': tform})

        return render(request, 'teacher_form.html', {'tform': tform})

    else:
        tform = Reg_Form()
        return render(request, 'teacher_form.html', {'tform': tform})



#   Authentication

def profile_view(request):

     if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            email_id = request.POST.get("email_id")

            password = request.POST.get("password")

            data = Reg_Model.objects.filter(email_id=email_id,password=password)

            if bool(data): 
                data = data.get()
                return render(request,'teacher-profile-page.html',{'data':data})
            else:
                return HttpResponse('invalid user data')
        else:
            return HttpResponse('Invalid User id And Password')



#  Login Form

def login_view(request):
    lform = LoginForm()
    return render(request, 'login.html', {'lform': lform})






# About Us

def about_view(request):
    return render(request, 'about.html')


def ad_fees(request):
    return render(request, 'admission_fees.html')


def fee_view(request):
    return render(request, 'fees.html')


def withdraw_view(request):
    return render(request, 'withdraw.html')


def facilities_view(request):
    return render(request, 'facilities.html')


#  Read More Section

def fac_read_more(request):
    return render(request, 'facilities_read_more.html')


def games_read_more(request):
    return render(request, 'games_read_more.html')


def new_read_more(request):
    return render(request, 'new_read_more.html')


def board_read_more(request):
    return render(request, 'boarding_read_more.html')


def acti_read_more(request):
    return render(request, 'activities_read_more.html')


def acad_read_more(request):
    return render(request, 'academics_read_more.html')





# What we do

def teachers(request):
    return render(request, 'teachers.html')

def parents(request):
    return render(request, 'parents.html')









## For 2nd User ##

# Student Portal

# def student_signup_view(request):
#     form = StudentForm(request.POST or None)
#
#     context = {'form': form}
#
#     if form.is_valid():
#         print(form.cleaned_data)
#
#         s_id = request.POST.get('s_id')
#         name = request.POST.get('name')
#         email_id = request.POST.get('email_id')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#
#         section = request.POST.get('section')
#         data = Student_Model(s_id=s_id, name=name, email_id=email_id,
#                              password=password, confirm_password=confirm_password
#                              , section=section)
#         data.save()
#         # sform = StudentForm()
#         # return render(request, 'student_form.html', {'sform': sform})
#
#     return render(request, 'student_form.html', context)
#     # else:
#     #     sform = StudentForm()
#     #     return render(request, 'student_form.html', {'sform': sform})


# Student Authentication
#
# def student_login_view(request):
#     email = request.POST.get("email_id")
#     password = request.POST.get("password")
#
#     e_id = Student_Model.objects.filter(email_id=email)
#     pwd = Student_Model.objects.filter(password=password)
#
#     if e_id and pwd:
#         return render(request, "student-profile-page.html")
#
#     else:
#         return render(request, "index.html")
