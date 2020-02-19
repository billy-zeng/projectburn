from django.shortcuts import render, redirect
from .forms import UserForm


def post_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = User(
            name=form.cleaned_data['name'],
            height=form.cleaned_data['height'],
            weight=form.cleaned_data['weight'],
            age=form.cleaned_data['age'],
            isMale=form.boolean_field(default=True),
            bmr=bmr(),
            targetweight=form.cleaned_data['targetweight'],
            goal=form.as_table['bulk', 'maintain_weight', 'lose_weight'],
        )

        User = form.save(commit = False)
        User.save()
        # return redirect('/')


bmr():
# Harris-Benedict Equation
    if isMale:
        bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

    bmr = round(bmr)
    print(bmr)




def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    # return redirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        # return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    # return redirect(/)