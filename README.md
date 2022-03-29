# easy-wordle
Wordle bot for [wordleplay.com](https://wordleplay.com/de/)

<img src="https://github.com/tobiaskeiner/easy-wordle/blob/main/new32223.gif" width=40% height=40%>

Word list in code is for the german version only.

The wordle game mode (letter amount) can easily be changed
```python
for word in word_list:
    if len(word) == 10:
        cur_list.append(word)
```
and
```python
driver.get("https://wordleplay.com/de/10-letter-words")
```
