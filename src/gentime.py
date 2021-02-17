def gen(times) -> int:
    """Calculate time for input start/time

    return count minute (h*60+m)-(h*60+m)
    example: 22:11-22:12
    return: 1

    input 25 for exit!!!

    return time for minute
    --
    test:

    >>> test.input_time()
    >>> '13:00-14:00'
    60
    >>> test.input_time()
    >>> '13:30-14:30'
    60
    >>> test.input_time()
    >>> '15:30-16:00'
    30
    >>> test.input_time()
    >>> '25:55-26:55'
    Fall: start time!!!
    0
    >>> test.input_time()
    >>> '18:30-16:30'
    Fall: Start time < stop time!!!
    0

    """

    times = times.split('-')
    start = times[0].split(':')
    stop = times[1].split(':')

    start_hour = int(start[0])
    start_min = int(start[1])
    stop_hour = int(stop[0])
    stop_min = int(stop[1])

    if start_hour > 24 or start_hour < 0\
            or stop_min > 60 or stop_min < 0:
        print('Fall: start time!!!', file=sys.stderr)
        return False
    elif stop_hour > 24 or stop_hour < 0\
            or stop_min > 60 or stop_min < 0:
        print('Fall: stop time!!!', file=sys.stderr)
        return False
    elif start_hour > stop_hour:
        print('Fall: Start time < stop time!!!', file=sys.stderr)
        return False
    else:
        return str((stop_hour * 60 + stop_min) - (start_hour * 60
                                               + start_min))
    return False
