from django.utils.timezone import localtime
from datetime import datetime, timezone


def get_duration(visit):
    entry_time = localtime(visit.entered_at)
    date_now = localtime(datetime.now(timezone.utc))
    if visit.leaved_at:
        different = date_now - entry_time
    else:
        different = visit.entered_at
    return different


def format_time(duration):
    time = duration.total_seconds()
    seconds_in_hour = 3600
    seconds_in_minute = 60
    minute_in_hour = 60
    hours = time // seconds_in_hour
    minutes = (time % seconds_in_hour) // minute_in_hour
    seconds = time % seconds_in_minute
    return f'{hours}:{minutes}:{seconds}'


def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        delta = visit.entered_at
    seconds = delta.total_seconds()
    seconds_in_hour = 3600
    seconds_in_minute = 60
    delta_minutes = ((seconds % seconds_in_hour) // seconds_in_minute) > minutes
    return delta_minutes

