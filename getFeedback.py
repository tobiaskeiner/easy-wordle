from re import search

def getFeedback(driver):
    table = driver.find_element_by_tag_name("table")
    first_locked_row = table.find_elements_by_class_name("Row Row-locked-in")[-1]
    columns = first_locked_row.find_elements_by_tag_name("td")

    position = 0
    out_letter = []
    yellow_letter = {}
    green_letter = {}

    for elem in columns:
        answer = elem.get_attribute("aria-label")
        if search("no", answer):
            out_letter.append(answer[0])
        elif search("elsewhere", answer):
            yellow_letter[answer[0].upper()] = position
        elif search("correct", answer):
            green_letter[answer[0].upper()] = position
        position += 1

    return out_letter, yellow_letter, green_letter