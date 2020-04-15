from django.shortcuts import render, redirect
from .models import Tutorial,UserRelationship,UserBlocked
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from .forms import TweetForm
from .forms import NewUserForm,AddFriendForm,DeleteFriendForm,DeleteFriendForm,BlockFriendForm,UnBlockFriendForm
global user_now

#some required functions to be used in the HomePageView class
user_now='null'
def friendsOf(username):
    friends = UserRelationship.objects.filter(selfname__exact=username)
    friendList = ''
    for friend in friends:
        friendList = friendList + '\n' + '\'' + friend.friendname + '\''
    return friendList
def friendlistOf(username):
    friends = UserRelationship.objects.filter(selfname__exact=username)
    friendList = []
    for friend in friends:
        friendList.append(friend.friendname)
    return friendList

def BeBlockedBy(username):
    friends = UserBlocked.objects.filter(selfname__exact=username)
    friendList = ''
    for friend in friends:
        friendList = friendList + '\n' + '\'' + friend.blockname + '\''
    return friendList

def BlockListBy(username):
    friends = UserBlocked.objects.filter(selfname__exact=username)
    friendList = []
    for friend in friends:
        friendList.append(friend.blockname)
    return friendList

# Create your views here.

#This is a class for the homepage. Tweets will show up here.
class HomePageView(TemplateView):
        
        
    #blist=BeBlockedBy(username)
    template_name = 'main/home.html'

    #This function will get the information from the database and user.
    def get(self, request):
        global user_now
        username=user_now
        form = TweetForm()
        flist=friendlistOf(username)
        blist=BlockListBy(username)
        tweets = Tweet.objects.all()
        new_tweets=[]
        for tweet in tweets:
            if str(tweet.user)==username or (str(tweet.user)in flist and str(tweet.user)not in blist):
                new_tweets.append(tweet)
        args = {'form': form, 'tweets': new_tweets}
        return render(request, self.template_name, args)
        
        #This function will display the information being retrieved.
    def post(self, request):
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
    global user_now
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                user_now=username
                return redirect('/homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
def account(request):
    global user_now
    username=user_now
    friendList = friendsOf(username)
    blockList = BeBlockedBy(username)
    if request.method == 'POST':
        if 'add' in request.POST:
            aff = AddFriendForm(request.POST)
            if aff.is_valid():
                friendWaitToAdd = aff.cleaned_data['friendWaitToAdd']
                isRelationExist = UserRelationship.objects.filter(selfname__exact=username,friendname__exact=friendWaitToAdd)
                isfFiendWaitToAddExist = User.objects.filter(username__exact=friendWaitToAdd)
                if not isfFiendWaitToAddExist:
                    context = {'error': 'friendWaitToAdd is not exist', 'username': username, 'friendList': friendList,
                               'blockList': blockList}
                    return render(request, 'main/account.html', context)
                else:
                    if isRelationExist:
                        context = {'error1': request.method, 'error': 'friendWaitToAdd is  already your friend',
                                   'username': username, 'friendList': friendList, 'blockList': blockList}
                        return render(request, 'main/account.html', context)
                    else:
                        UserRelationship.objects.create(selfname=username, friendname=friendWaitToAdd)
                        friendList = friendsOf(username)
                        context = {'error': 'done', 'username': username, 'friendList': friendList,
                                   'blockList': blockList}
                        return render(request, 'main/account.html', context)
            else:
                context = {'username': username, 'friendList': friendList, 'blockList': blockList}
                return render(request, 'main/account.html', context)

        elif 'delete' in request.POST:
            dff = DeleteFriendForm(request.POST)
            if dff.is_valid():
                friendWaitToDelete = dff.cleaned_data['friendWaitToDelete']
                isRelationExist = UserRelationship.objects.filter(selfname__exact=username,
                                                                  friendname__exact=friendWaitToDelete)
                isfFiendWaitToDelete = User.objects.filter(username__exact=friendWaitToDelete)
                if not isfFiendWaitToDelete:
                    context = {'error': 'friendWaitToDelete is not exist', 'username': username,
                               'friendList': friendList, 'blockList': blockList}
                    return render(request, 'main/account.html', context)
                else:
                    if not isRelationExist:
                        context = {'error': 'friendWaitToDelete is not your friend', 'username': username,
                                   'friendList': friendList, 'blockList': blockList}
                        return render(request, 'main/account.html', context)
                    else:
                        UserRelationship.objects.filter(selfname=username, friendname=friendWaitToDelete).delete()
                        friends = UserRelationship.objects.filter(selfname__exact=username)
                        friendList = ''
                        for friend in friends:
                            friendList = friendList + '\n' + '\'' + friend.friendname + '\''
                        context = {'error': 'done', 'username': username, 'friendList': friendList,
                                   'blockList': blockList}
                        return render(request, 'main/account.html', context)
            else:
                context = {'username': username, 'friendList': friendList, 'blockList': blockList}
                return render(request, 'main/account.html', context)
        elif 'block' in request.POST:
            bff = BlockFriendForm(request.POST)
            if bff.is_valid():
                friendWaitToBlock = bff.cleaned_data['friendWaitToBlock']
                isRelationExist = UserBlocked.objects.filter(selfname__exact=username,
                                                             blockname__exact=friendWaitToBlock)
                isfFiendWaitToBlock = User.objects.filter(username__exact=friendWaitToBlock)
                if not isfFiendWaitToBlock:
                    context = {'error': 'friendWaitToBlock is not exist', 'username': username,
                               'friendList': friendList, 'blockList': blockList}
                    return render(request, 'main/account.html', context)
                else:
                    if isRelationExist:
                        context = {'error': 'already blocked', 'username': username, 'friendList': friendList,'blockList': blockList}
                        return render(request, 'main/account.html', context)
                    else:
                        UserBlocked.objects.create(selfname=username, blockname=friendWaitToBlock)
                        blockList = BeBlockedBy(username)
                        context = {'error': 'done', 'username': username, 'friendList': friendList,
                                   'blockList': blockList}
                        return render(request, 'main/account.html', context)
            else:
                context = {'username': username, 'friendList': friendList, 'blockList': blockList}
                return render(request, 'main/account.html', context)
        elif 'unblock' in request.POST:
                ubf=UnBlockFriendForm(request.POST)
                if ubf.is_valid():
                        friendWaitToUnBlock = ubf.cleaned_data['friendWaitToUnBlock']
                        isRelationExist = UserBlocked.objects.filter(selfname__exact=username,
                                                             blockname__exact=friendWaitToUnBlock)
                        isfFiendWaitToUnBlock = User.objects.filter(username__exact=friendWaitToUnBlock)
                        if not isfFiendWaitToUnBlock:
                                context = {'error': 'friendWaitToUnblock is not exist', 'username': username,'friendList': friendList, 'blockList': blockList}
                                return render(request, 'main/account.html', context)
                        else:
                                if not isRelationExist:
                                        context = {'error': 'not in your block list', 'username': username, 'friendList': friendList,'blockList': blockList}
                                        return render(request, 'main/account.html', context)
                                else:
                                        UserBlocked.objects.filter(selfname=username, blockname=friendWaitToUnBlock).delete()
                                        blockList = BeBlockedBy(username)
                                        context = {'error': 'done', 'username': username, 'friendList': friendList,'blockList': blockList}
                                        return render(request, 'main/account.html', context)
                else:
                        context = {'username': username, 'friendList': friendList, 'blockList': blockList}
                        return render(request, 'main/account.html', context)        
                
    else:
        context = {'username': username, 'friendList': friendList, 'blockList': blockList}
        return render(request, 'main/account.html', context)
