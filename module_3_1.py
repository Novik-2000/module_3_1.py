calls = 0


def count_calls(n):
    calls = n
    return calls


r = count_calls('Capybara')
w = count_calls('armageddon')


def string_info(h):
    zero = (len(h), h.upper(), h.lower())
    return zero


print(string_info(r))
print(string_info(w))


def is_contains(string, list_to_search):
    if print(string in list_to_search) == True:
        print(True)
    else:
        print(False)

print(is_contains('Urban', ['ban', 'BaNaN', 'Urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)