from django.http import HttpResponse ,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm , UserEditForm, ProfileEditForm ,MemberForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Member
from django.views.generic import ListView, DetailView


from django.contrib.auth.decorators import login_required, user_passes_test


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,
    'account/dashboard.html',
    {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
            'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})



class MemberListView(ListView):
    model = Profile
    template_name = 'account/member_list.html'
    context_object_name = 'members'



class MemberListView(ListView):
    model = Member
    template_name = 'account/member_list.html'
    context_object_name = 'members'



@login_required
def dashboard(request):
    members = Profile.objects.all()
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'members': members})

#########


@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'account/member_list.html', {'members': members})

@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'account/member_detail.html', {'member': member})

@user_passes_test(lambda u: u.is_superuser)
def member_add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'account/member_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'account/member_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def member_remove(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_list')

