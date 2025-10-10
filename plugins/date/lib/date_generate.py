from datetime import datetime, timedelta, timezone

def get_today(tz=None):
    now = datetime.now(timezone.utc)
    if tz is not None:
        try:
            offset = int(tz)
            now = now + timedelta(hours=offset)
        except Exception:
            pass
    return now.strftime("%Y-%m-%d")