def correct_sentence(text):
    if text[0].islower(): text = text.capitalize()
    #if not (text[-1].isalpha() or text[-1] == '.'): text += '.'
    if not text.endswith('.'): text += '.'
    return text


# correct_sentence("greetings, friends")

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
