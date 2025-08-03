import pandas as pd
from main import syllabificate_word
import re

subtlex = pd.read_excel('subtlex_v2_cleaned_no_drop3.xlsx')
print(subtlex)


def is_valid(word):
    return isinstance(word, str) and re.fullmatch(r"[a-zA-Zäëïöüáéíóúâêîôûç\-']+", word)

invalid_words = []
error_words = []

for i, row in subtlex.iterrows():
    word = row['Word']
    if is_valid(word):
        try:
            syll = syllabificate_word(word, alg='n', language='nl')
            print(f"Syllabifying {word}, result = {syll}")
        except Exception as e:
            error_words.append((word, str(e)))
            syll = ''
    else:
        invalid_words.append(word)
        syll = ''
    subtlex.loc[i, 'Syllabification'] = syll
    
subtlex.to_csv('subtlex_syllabified.csv')
print("Invalid words (bad characters):", invalid_words[:10])
print("Words that caused exceptions:", error_words[:10])