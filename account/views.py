from django.http import HttpResponse ,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm , UserEditForm, ProfileEditForm ,MemberForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Member
from django.views.generic import ListView, DetailView
from events.models import Event,News

from .forms import UserRegistrationForm


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
            new_user = user_form.save()
            # Log the user in after registration
            login(request, new_user)
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
    members = Member.objects.all()
    profiles = Profile.objects.all()
    total_profiles = profiles.count()
    total_members = members.count()

    total_events = Event.objects.count()
    total_news = News.objects.count()

    # Example data for a pie chart
    chart_data = {
        'labels': ['Members', 'Events', 'News','Profiles'],
        'data': [total_members, total_events, total_news,total_profiles],
        'backgroundColor': ['#36A2EB', '#FF6384', '#FFCE56','#0529C92A'],
    }
    bar_chart_data = {
        'labels': ['Members', 'Events', 'News','Profiles'],
        'data': [total_members, total_events, total_news ,total_profiles],
        'backgroundColor': ['#0F8A04', '#CCBF0B', '#FF5C56','#0529C92A'],
    }

    return render(
        request,
        'account/dashboard.html',
        {
            'section': 'dashboard',
            'total_profiles':total_profiles,
            'profile_members': members,
            'total_members': total_members,
            'total_events': total_events,
            'total_news': total_news,
            'chart_data': chart_data,
            'bar_chart_data': bar_chart_data,
        }
    )

#########



class MemberListView(ListView):
    model = Member
    template_name = 'account/member_list.html'
    context_object_name = 'members'
    ordering = ['name']  
    def get_queryset(self):
        return Member.objects.all()


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

