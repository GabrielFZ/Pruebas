from collections import defaultdict
import os


def get_signature(word):
    signature = defaultdict(int)
    for char in word:
        signature[char] += 1

    return signature
    

def annograms(word):    
    word = word.replace(" ", "").lower()    
    word_len = len(word)    
    word_signature = get_signature(word)

    dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(dir, 'WORD.lst')
    
    words = [w.rstrip() for w in open(file)]
    annagrams = []

    for candidate in words:
        if word_len != len(candidate):
            continue

        signature = get_signature(candidate)
        if signature == word_signature:            
            annagrams.append(candidate)

    return annagrams


if __name__ == "__main__":    
    print(annograms("Train"))
    print('--')
    print(annograms('Drive'))
    print('--')
    print(annograms('Python'))
    
    