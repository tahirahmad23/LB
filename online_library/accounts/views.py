from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import User,Uploader
from .forms import UserForm, Loginform, CreateUploaderForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class SignUp(CreateView):

    model = User
    template_name = "signup.html"
    form_class = UserForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()

        user = authenticate(email=form.cleaned_data["email"],password=form.cleaned_data["password1"])
        if user != None:
            login(self.request,user)
            return redirect("home")
        else:
            print("failed")

        return super().form_valid(form)

class CreateUploader(CreateView):
    model = Uploader
    # fields = "__all__"
    form_class = CreateUploaderForm
    template_name = "uploaderform.html"
    success_url = reverse_lazy("home")

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = User.objects.get(username=self.request.user.username)
        self.object.save()
        return super().form_valid(form)

def loginuser(request):

    form = Loginform()

    if request.method == "POST" :
        form = Loginform(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.get(email=email)
            user = authenticate(email=email,password=password)


            if user:
                login(request,user)
                return redirect("home")
            else:
                print(user)
    return render(request, "login.html",{"form":form})

def logout_user(request):

    logout(request)
    return redirect("home")
