from django.shortcuts import render, redirect
from .models import Tutorial
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from .forms import TweetForm




# Create your views here.

#This is a class for the homepage. Tweets will show up here.
class HomePageView(TemplateView):
        template_name = 'main/home.html'

        #This function will get the information from the database and user.
        def get_tweet(self, request):
                form = TweetForm()
                tweets = Tweet.objects.all()

                args = {'form': form, 'tweets': tweets}
                return render(request, self.template_name, args)
        
        #This function will display the information being retrieved.
        def post_tweet(self, request):
                form = TweetForm(request.POST)
                if form.is_valid():

                        tweet = form.save(commit=False)
                        tweet.user = request.user
                        tweet.save()

                        
                        content = form.cleaned_data['tweet_content']
                        form = TweetForm()
                        messages.info(request, f"Tweet sent")
                        return redirect('main:homepage')
                        

                args = {'form': form, 'content': content}
                return render(request, self.template_name, args)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect("main:login")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
