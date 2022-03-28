from re import search
from typing import List

def getFeedback(row,driver):
    table = driver.find_element_by_tag_name("table")
    rows = table.find_elements_by_tag_name("tr")
    columns = rows[row].find_elements_by_tag_name("td")
    

    position = 0
    out_letter = []
    yellow_letter = []
    green_letter = []

    for elem in columns:
        answer = elem.get_attribute("aria-label")
        if search("no", answer):
            out_letter.append(answer[0])
        elif search("elsewhere", answer):
            yellow_letter.append([answer[0].upper(), position])
        elif search("correct", answer):
            green_letter.append([answer[0].upper(), position])
        position += 1

    print(out_letter,yellow_letter,green_letter)
    return out_letter, yellow_letter, green_letter