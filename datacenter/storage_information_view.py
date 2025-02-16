from datacenter.models import Passcard, Visit, get_duration, format_time
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in leaved:
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
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

