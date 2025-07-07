from datacenter.models import Passcard, Visit
from django.shortcuts import render
from datacenter.security_info_helper import get_duration, format_time


def storage_information_view(request):
    leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in leaved_visits:
        duration = get_duration(visit)
        visit_time = format_time(duration)
        person = visit.passcard
        non_closed_visits.append(
            {
                'who_entered': person,
                'entered_at': visit_time,
                'duration': duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
