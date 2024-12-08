from django.shortcuts import render, redirect, get_object_or_404
from .models import Group


def home(request):
    return render(request, 'index.html')


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/group-list.html', ctx)


def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_type = request.POST.get('group_type')



        if (group_name and group_type):
            Group.objects.create(
                group_name=group_name,
                group_type=group_type,

            )
            return redirect('groups:list')

    return render(request, 'groups/group-form.html')



def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')
