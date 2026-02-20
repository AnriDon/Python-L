def second_index(text, some_str):
    res = None
    if text.count(some_str) > 1:
        text = text.replace(some_str, "", 1)
        res = text.find(some_str) + len(some_str)
    return res


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
