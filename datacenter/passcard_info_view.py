from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datetime import datetime, timezone



def get_duration(visit):
    entry_time = localtime(visit.entered_at)
    date_now = localtime(datetime.now(timezone.utc))
    different = date_now - entry_time
    return different

def format_time(duration):
    time = duration.seconds
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60
    return f'{hours}:{minutes}:{seconds}'

def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        delta = visit.entered_at
    seconds = delta.seconds
    delta_minutes = (seconds % 3600) // 60
    if delta_minutes > minutes:
        return True
    return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    leaved = Visit.objects.filter(passcard=passcard)
    for visit in leaved:
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
