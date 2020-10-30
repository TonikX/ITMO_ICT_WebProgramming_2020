from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Car, RacerProfile, Race, Comment
from .forms import AddCommentForm, RacerProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from registration.backends.simple.views import RegistrationView

def main(request):
    return render(request, 'main_page.html')


def register_profile(request):
    form = RacerProfileForm
    if request.method == 'POST':
        form = RacerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            form.save()
            return redirect(reverse('main'))
        else:
            print(form.errors)

    return render(request, 'registration/profile_registration.html', {'form': form})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

def leaderboard_view(request):
    races = Race.objects.all()
    winners = [race.winner for race in races]
    racers = RacerProfile.objects.filter(name__in=winners)
    car_names = [racer.car for racer in racers]
    cars = Car.objects.filter(description__in=car_names)
    return render(request, 'leaderboard_view.html', {'info': zip(races, racers, cars)})


def comments(request):
    # all comments
    comments = {}
    comments['comments'] = Comment.objects.all()

    # form
    form = AddCommentForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        form.user = request.user
        form.save()
        return redirect('comments')
    comments['form'] = form

    return render(request, 'comments.html', comments)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        userprofile = RacerProfile.objects.get_or_create(user=user)[0]
        form = RacerProfileForm({'picture': userprofile.picture})
        return user, userprofile, form

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('main'))
        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form}
        return render(request, 'profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('main'))
        form = RacerProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=False)
            return redirect(reverse('main'), user.username)
        else:
            print(form.errors)
        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form}
        return render(request, 'profile.html', context_dict)


def logout_request(request):
    logout(request)
    return redirect(reverse('main'))
