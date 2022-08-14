__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds < 60:
        return '{:02}s'.format(seconds)
    elif seconds < 3600:
        minute = seconds // 60
        sec = seconds - 60 * minute
        return '{:02}m{:02}s'.format(minute,
                                     sec
                                     )
    elif seconds < 86400:
        h = seconds // 3600
        minute = (seconds - h * 3600) // 60
        sec = (seconds - (h * 3600 + minute * 60))
        return '{:02}h{:02}m{:02}s'.format(h,
                                           minute,
                                           sec
                                           )
    else:
        day = seconds // 86400
        h = (seconds - (day * 86400)) // 3600
        minute = (seconds - (day * 86400 + h * 3600)) // 60
        sec = seconds - (day * 86400 + h * 3600 + minute * 60)
        return '{:02}d{:02}h{:02}m{:02}s'.format(day,
                                                 h,
                                                 minute,
                                                 sec
                                                 )




