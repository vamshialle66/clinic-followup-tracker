from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FollowUp, UserProfile
from .forms import FollowUpForm
from django.http import Http404
from .models import FollowUp, PublicViewLog
from django.db.models import Count

@login_required
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    clinic = user_profile.clinic

    followups = (
        FollowUp.objects
        .filter(clinic=clinic)
        .annotate(view_count=Count('publicviewlog'))
    )

    context = {
        'followups': followups,
        'total_count': followups.count(),
        'pending_count': followups.filter(status='pending').count(),
        'done_count': followups.filter(status='done').count(),
    }

    return render(request, 'dashboard.html', context)

@login_required
def create_followup(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = FollowUpForm(request.POST)
        if form.is_valid():
            followup = form.save(commit=False)
            followup.clinic = user_profile.clinic
            followup.created_by = request.user
            followup.save()
            return redirect('dashboard')
    else:
        form = FollowUpForm()

    return render(request, 'create_followup.html', {'form': form})

@login_required
def edit_followup(request, pk):
    followup = get_object_or_404(
        FollowUp,
        pk=pk,
        clinic__userprofile__user=request.user
    )

    if request.method == 'POST':
        form = FollowUpForm(request.POST, instance=followup)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FollowUpForm(instance=followup)

    return render(request, 'edit_followup.html', {'form': form})

@login_required
def mark_done(request, pk):
    followup = get_object_or_404(
        FollowUp,
        pk=pk,
        clinic__userprofile__user=request.user
    )
    followup.status = 'done'
    followup.save()
    return redirect('dashboard')

def public_followup(request, token):
    try:
        followup = FollowUp.objects.get(public_token=token)
    except FollowUp.DoesNotExist:
        raise Http404("Invalid link")

    PublicViewLog.objects.create(
        followup=followup,
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        ip_address=request.META.get('REMOTE_ADDR')
    )


    if followup.language == 'hi':
        message = "आपका फॉलो-अप सफलतापूर्वक दर्ज किया गया है।"
    else:
        message = "Your follow-up has been recorded successfully."

    return render(request, 'public_followup.html', {
    'patient_name': followup.patient_name,
    'due_date': followup.due_date,
    'status': followup.status,
    'message': message
})
