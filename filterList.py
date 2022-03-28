def out(word, out_letter):
    for letter in word:
        for out in out_letter:
            if letter.upper() == out:
                return True

def yellow(word, yellow_letter):
    for y_letter in yellow_letter:
        if  not(y_letter in word.upper() and word[yellow_letter[y_letter]].upper() != y_letter):
            return True

def green(word, green_letter):
    for g_letter in green_letter:
        if word[green_letter[g_letter]].upper() != g_letter:
            return True

def filterWords(word, yellow_letters, green_letters, out_letters):
    if out(word, out_letters):
        return False
    elif yellow(word, yellow_letters):
        return False
    elif green(word, green_letters):
        return False
    else:
        return True