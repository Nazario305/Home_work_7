def second_index(text, some_str):

    some_str_index = text.find(some_str)
    result = text.find(some_str, some_str_index + len(some_str))

    # print(text.find(some_str))
    # print(result)

    if result != -1:
        return result
    else:
        return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# second_index("sims", "s")