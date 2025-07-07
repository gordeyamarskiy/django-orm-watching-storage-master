from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.security_info_helper import get_duration, format_time, \
    is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    leaved_visits = Visit.objects.filter(passcard=passcard)
    for visit in leaved_visits:
        duration = get_duration(visit)
        visit_time = format_time(duration)
        entered_at = localtime(visit.entered_at)
        is_strange = is_visit_long(visit)
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': visit_time,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
