from cProfile import Profile
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task, Profile
from django.db.models import Q



# Create your views here.
def my_recommendations_view(request):
    profile=Profile.objects.get(user=request.user)
    my_recs=profile.get_recommend_profiles()
    print("my_recs:", my_recs)
    rewards=len(my_recs)*20
    context={'my_recs':my_recs,'rewards':rewards}
    return render(request,'profiles/main.html',context)




def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Assigning the user directly
            task.save()
            form.save_m2m()  # Save the many-to-many relationship
            return redirect('task_list')
    else:
        profile = Profile.objects.get(user=request.user)
        my_recs = profile.get_recommend_profiles()
        user_list = [profile.user for profile in my_recs]  # Extracting users from my_recs
        print("User List:", user_list)  # Print the user list for troubleshooting
        form = TaskForm(user=request.user, user_list=user_list)  # Pass user_list to the form
        print("Form:", form)  # Print the form for troubleshooting
    return render(request, 'profiles/create_task.html', {'form': form , 'user_list': user_list})


def task_list(request):
    profile = Profile.objects.get(user=request.user)
    user = profile.user  # Retrieve the User instance associated with the profile
    tasks = Task.objects.filter(Q(created_by=user) | Q(shared_with=user))
    return render(request, 'profiles/task_list.html', {'tasks': tasks})