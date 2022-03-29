# easy-wordle
Wordle bot for [wordleplay.com](https://wordleplay.com/de/)

Word list in code is for the german version only.

The wordle game mode can easily be changed
```python
for word in word_list:
    if len(word) == 10:
        cur_list.append(word)
```
and
```python
driver.get("https://wordleplay.com/de/10-letter-words")
```
