from django.test import TestCase

# Create your tests here.
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.shortcuts import render, redirect
# from django.contrib import messages
#
# def registration(request):
#     if request.method == 'POST':
#         USERNAME = request.POST.get('Username')
#         FIRST_NAME = request.POST.get('First_Name')
#         LAST_NAME = request.POST.get('Last_Name')
#         EMAIL = request.POST.get('Email')
#         PASSWORD = request.POST.get('Password')
#         CONFORM_PASSWORD = request.POST.get('Conform_password')
#
#         if PASSWORD == CONFORM_PASSWORD:
#             # Use Django's built-in validators for password strength
#             try:
#                 User.objects.get(username=USERNAME)
#                 messages.info(request, 'Error: That username is already taken')
#                 return redirect('register')
#             except User.DoesNotExist:
#                 pass  # Username is not taken
#
#             try:
#                 User.objects.get(email=EMAIL)
#                 messages.info(request, 'E-mail id is already taken')
#                 return redirect('register')
#             except User.DoesNotExist:
#                 pass  # Email is not taken
#
#             # Validate password strength using Django's built-in validators
#             from django.contrib.auth.password_validation import validate_password
#             try:
#                 validate_password(PASSWORD)
#             except ValidationError as e:
#                 messages.error(request, '\n'.join(e))
#                 return redirect('register')
#
#             # Create user
#             user = User.objects.create_user(
#                 username=USERNAME,
#                 email=EMAIL,
#                 password=PASSWORD,
#                 first_name=FIRST_NAME,
#                 last_name=LAST_NAME
#             )
#             user.save()
#             messages.success(request, 'Successfully Created an Account')
#             return redirect('home')  # Adjust to your post-registration URL
#         else:
#             messages.error(request, 'Check Password')
#             return redirect('register')
#     return render(request, 'registration.html')