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
