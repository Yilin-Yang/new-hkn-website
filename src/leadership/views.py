from hknWebsiteProject import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LeaderModelForm, DeleteLeaderForm
from .models import Leader
from users.models import Member
# Create your views here.
from django.forms import modelformset_factory


def leadership(request, leader_saved=0):
    context = {}
    officers = Leader.objects.all().filter(position_type__exact='O').filter(
        member__isnull=False).order_by('-display_order')
    advisors = Leader.objects.all().filter(position_type__exact='A').filter(
        member__isnull=False).order_by('-display_order')
    chairs = Leader.objects.all().filter(position_type__exact='C').filter(
        member__isnull=False).order_by('-display_order')
    context['officers'] = officers
    context['advisors'] = advisors
    context['chairs'] = chairs
    context['leader_saved'] = leader_saved
    return render(request, "leadership/leadership.html", context)


@login_required()
def edit_leadership(request, position_added=0):
    context = {}
    if not request.user.is_superuser:
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        leaders = Leader.objects.all().order_by('-display_order')
        context = {
            'leaders': leaders,
            'position_added': position_added
        }

        LeaderFormSet = modelformset_factory(Leader, fields=('member',), extra=0)
        leader_form = LeaderFormSet(queryset=Leader.objects.all().order_by('-display_order'))
        context['leader_form'] = leader_form

        if request.POST:
            formset = LeaderFormSet(request.POST)
            formset.save()

            # Remove officer status from old leaders
            old_leaders = Member.objects.filter(status__exact='O');
            for m in old_leaders:
                m.status = 'A'
                m.save()

            # Add officer status to new leaders
            all_leaders = Leader.objects.all()
            for l in all_leaders:
                if l.member is not None:
                    l.member.status = 'O'
                    l.member.save()

            return redirect('leadership', leader_saved=1)

    return render(request, "leadership/edit_leadership.html", context)


@login_required()
def add_leadership(request):
    context = {}
    if not request.user.is_superuser:
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        form = LeaderModelForm()
        context['form'] = form

        if request.POST:
            form = LeaderModelForm(request.POST)
            form.save()
            return redirect('edit_leadership', position_added=1)

    return render(request, "leadership/add_leadership.html", context)

@login_required()
def delete_leader(request):
    context = {}
    form = DeleteLeaderForm()
    context['form'] = form

    if request.POST:
        form = DeleteLeaderForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data.get('delete_leader').position
            leader = Leader.objects.get(position__exact=position)
            leader.delete()
            return redirect('edit_leadership', position_added=1)
    return render(request, "leadership/delete_leader.html", context)
