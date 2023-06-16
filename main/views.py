from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from main.forms import CommentForm, RegistrationForm, CustomUserChangeForm
from main.models import Comment, Profile


def index(request):
    return render(request, 'main.html')


def animals(request):
    return render(request, 'animals.html')


def care(request):
    return render(request, 'care.html')


def finder(request):
    return render(request, 'finder.html')


def account(request):
    return render(request, 'account.html')


def register(request):
    form = RegistrationForm()
    if "register" in request.POST:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                user_username = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                new_user.set_password(user_password)
                new_user.save()
                user = authenticate(username=user_username, password=user_password)
                login(request, user)
                return render(request, 'account.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'account.html')
            else:
                form = RegistrationForm()
    return render(request, 'profile.html', {'form': form})


def get_comments(request):
    comments = Comment.objects.all()
    data = []
    for comment in comments:
        data.append({
            'name': comment.name,
            'content': comment.content,
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def comment_form(request):
    form = CommentForm()
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                content=form.cleaned_data['content'],
            )
            comment.save()
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
    return render(request, "main.html", {"form": form})


def update_account(request):
    form = CustomUserChangeForm()
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            user = Profile(
                nickname=form.cleaned_data['nickname'],
                bio=form.cleaned_data['bio'],
                profile_pic=form.cleaned_data['profile_pic'],
            )
            user.save()
            return render(request, 'account.html')
        else:
            form = CustomUserChangeForm()
    return render(request, 'account.html', {'form': form})
