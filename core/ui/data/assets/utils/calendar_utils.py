from datetime import datetime, timedelta

def get_available_slots(start_hour=8, end_hour=20, slot_duration=1.0):
    """
    Returns a list of available hourly time slots in a day.
    """
    slots = []
    current = datetime.now().replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end = current.replace(hour=end_hour)
    while current < end:
        slots.append(current.strftime('%H:%M'))
        current += timedelta(hours=slot_duration)
    return slots

def get_current_week_dates():
    """
    Returns list of dates for the current week starting from today.
    """
    today = datetime.today()
    return [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
