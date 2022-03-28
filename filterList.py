def out(word, out_letter):
    for letter in word:
        for elem in out_letter:
            if letter.upper() == elem:
                return True

def yellow(word, yellow_letter):
    for element in yellow_letter:
        if word[element[1]].upper() == element[0] or element[0] not in word.upper():
            return True

def green(word, green_letter):
    for element in green_letter:
        if word[element[1]].upper() != element[0]:
            return True

def filterWords(word, yellow_letters, green_letters, out_letters):
    if out(word, out_letters):
        return True
    elif yellow(word, yellow_letters):
        return True
    elif green(word, green_letters):
        return True
    else:
        return False