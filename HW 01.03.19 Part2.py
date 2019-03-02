def reverse_list(first, last, step=-1):
    current = first
    end = last

    if first < last:
        raise ValueError("A can not be < B!")

    if step == 0:
        raise ValueError("Step must not be zero")

    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step

lst = reverse_list(10, 2)
try:
    while True:
        print(next(lst))
except StopIteration:
    print()