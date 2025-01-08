def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('email')

        try:
            user = Login.objects.get(email=username)

        except Login.DoesNotExist:
            user = None

        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'rahulinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = Login.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent successfully to your registered email')
            return redirect(indexpage)
        else:
            messages.info(request, 'This account does not exist')
    return redirect(indexpage)





# SETTINGS.PY EMAIL VARIABLES

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'YOUR ACCOUNT'
# EMAIL_HOST_PASSWORD = 'YOUR APP PASSWORD'
