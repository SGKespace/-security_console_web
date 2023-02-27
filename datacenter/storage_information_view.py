from django.shortcuts import render
from django.utils import timezone

from datacenter.models import get_duration, format_duration, is_visit_long
from datacenter.models import Visit



def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        visit_element = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
                        }
        non_closed_visits.append(visit_element)

    context = {
        'non_closed_visits': non_closed_visits,
              }

    return render(request, 'storage_information.html', context)