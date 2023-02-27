from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from datacenter.models import get_duration, format_duration, is_visit_long

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        time_delta = get_duration(passcard_visit)

        visit = {
            'entered_at': passcard_visit.entered_at,
            'duration': format_duration(time_delta),
            'is_strange': is_visit_long(passcard_visit),
                 }

        this_passcard_visits.append(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
               }

    return render(request, 'passcard_info.html', context)
