def in_range(start, end, step=1):
    result = []
    if step > 0:
        while start < end:
            result.append(start)
            start += step
    elif step < 0:
        while start > end:
            result.append(start)
            start += step
    return result
print(in_range(3,5))