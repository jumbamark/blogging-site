from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from theBlog.models import Profile


# Create your views here.


class UserRegistrationView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy("home")

    # telling the template what user we are
    def get_object(self):
        return self.request.user  # will pass in the current user


class ChangePasswords(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, 'registration/password-success.html', {})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["Page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = "__all__"

    success_url = reverse_lazy("home")

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    # fields = "__all__"
    template_name = 'registration/create_user_profile_page.html'

# we are making the user id available to our profile so that when we save the form it gets saved under the right user
    # set up some code that allows our project to figure out what user is filling that form (we are not using js)
    # the form will pass the user and then we can sort of hijack the form as it's being processed and pause that processing, insert back the user and continue with the processing

    def form_valid(self, form):
        # hey take 7,put it on the form as the user then save the form
        form.instance.user = self.request.user  #there's a user filling out this form, let's grab that user and make it available to the form itself
        return super().form_valid(form) #sort of save the form itself, passing in the form itself that has been submitted from the page