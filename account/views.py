from django.contrib.messages.api import MessageFailure
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from account.forms import RegisterUserForm, UpdateProfileForm
from account.helpers import search_profiles
from account.models import Profile
from portefolio.models import Project


# Create your views here.


def logoutUser(request):
    logout(request)
    messages.info(request, 'You are deconnected !')
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('list_of_article')
    form = RegisterUserForm
    if request.method == "POST":

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Account successfully created !')
            login(request, user)
            return redirect('list_of_article')
        else:
            messages.error(request, 'the form is not valid !')

    template = 'account/login.html'
    data = {'form': form, 'page': 'register'}
    return render(request, template_name=template, context=data)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('list_of_article')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:

            messages.error(request, 'user does not exist !')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'user connected !')
            return redirect('list_of_article')
        else:
            messages.warning(request, 'credentials are wrong !')
    template = 'account/login.html'
    data = {'page': 'login'}
    return render(request, template_name=template, context=data)


def profiles(request):

    # ----------------------------------------

    profiles, keyword = search_profiles(request)

    item_per_page = 3
    page = request.GET.get("page")
    paginator = Paginator(profiles, item_per_page)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    context = {"profiles": profiles,
               "keyword": keyword}

    return render(request, template_name='account/profiles.html', context=context)


def show(request, id):

    # try:
    #     article = Article.objects.get(slug=slug)
    # except:
    #     raise Http404
    profile = get_object_or_404(Profile, id=id)

    projects = Project.objects.filter(profile=profile)

    return render(request, "account/profile.html", {"profile": profile, "projects": projects})


def edit(request, id):

    if request.method == "POST":
        profile = get_object_or_404(Profile, id=id)
        print(profile)
        form = UpdateProfileForm(instance=profile)

        return render(request, "account/edit-profile.html", {"profile": profile, "form": form})
    return HttpResponse("You are not allowed to do that !")


def update(request, id):

    if request.method == "POST":
        profile = get_object_or_404(Profile, id=id)
        form = UpdateProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            projects = Project.objects.filter(profile=profile)
            return render(request, "account/profile.html", {"profile": profile, "projects": projects})
        return redirect("profiles-list")
