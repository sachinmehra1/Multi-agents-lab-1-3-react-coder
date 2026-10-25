import string

def word_frequency(filepath: str) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
