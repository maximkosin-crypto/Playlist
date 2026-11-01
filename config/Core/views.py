from django.shortcuts import render
import random
def magic_number(request):
    message = ""
    if "secret_number" not in request.session:
        request.session["secret_number"] = random.randint(1,2)

    if request.method == "POST":
        user_guess = request.POST.get("user_number")

        user_guess = int(user_guess)
        secret_number = request.session["secret_number"]
        if user_guess == secret_number:
            message = f"вы угадали было загадано {secret_number}"
        else: 
            message = f"вы не угадали было загадано {secret_number}"
            
    return render(request, "magic_number.html", {"message": message})
