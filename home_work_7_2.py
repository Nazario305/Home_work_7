def correct_sentence(text):
    text_update = text[0].upper()
    result = text_update + text[1:]
    if result[-1] == '.':
        # print(result)
        return result
    else:
        # print(result + '.')
        return result + '.'



assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

# correct_sentence("hello.")