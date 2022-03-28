def getBestWord(list, letterCount):
    list_scores = {}
    for word in list:
        scores = 0
        word_letters = []
        for letter in word:
            if letter not in word_letters:
                scores += letterCount[letter.upper()]
                word_letters.append(letter)
        list_scores[word] = scores

    return max(list_scores, key=list_scores.get)
    