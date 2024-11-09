def enough(cap, on, wait):
    total_passengers = on + wait
    if total_passengers <= cap:
        return 0
    else:
        return total_passengers - cap
