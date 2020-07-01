import nltk
import re
from nltk.stem import LancasterStemmer
from nltk import WordNetLemmatizer
from nltk.util import ngrams
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

def read_file(filename):
    '''
    Returns the content of a file
    :param filename: input filename
    :return: string
    '''
    with open(filename, 'r', encoding='utf-8') as filein:
        data = filein.read()
        return data

def tokenize(data):
    '''
    Tokenize the string into sentence and word tokens
    :param data: string data
    :return: sentence token and word token
    '''
    sentence_tokens = nltk.sent_tokenize(data)
    # to remove the punctuation to get the words
    data = re.sub(r'[^\w\s]', '', data)
    word_tokens = nltk.word_tokenize(data)
    return sentence_tokens, word_tokens

def pos_tag(word_list):
    '''
    Returns the Part of Speech tagging
    :param word_list: list of word tokens
    :return: tuple of (word, POS)
    '''
    return nltk.pos_tag(word_list)

def stem(word_list):
    '''
    Returns the stemming for a lisf of word
    :param word_list: list of words
    :return: list of tuple (word, stemming)
    '''
    result = []
    lstemmer = LancasterStemmer()
    for word in word_list:
        w = lstemmer.stem(word)
        result.append(w)
    return result

def lemmatize(word_list):
    '''
    Returns the lemmatization of a word
    :param word_list: list of words
    '''
    result = []
    lemmatizer = WordNetLemmatizer()

    for word in word_list:
        w = lemmatizer.lemmatize(word)
        result.append(w)
    return result

def trigram(sentence_list):
    '''
    Retwurns the triagram of a list of words
    :param sentence_list: list of words
    '''
    result = {}
    for sentence in sentence_list:
        token = nltk.word_tokenize(sentence)
        ng = list(ngrams(token,3))
        result[sentence] = ng
    return result

def ner(sentence_list):
    '''
    Returns the list of the Named Entity Recognition
    '''

    result = {}
    for sentence in sentence_list:
        ne = ne_chunk(pos_tag(wordpunct_tokenize(sentence)))
        result[sentence] = ne
    return result

def put_headline(headline):
    '''
    Prints a headline on the screen as separator
    '''
    print()
    print('#' * 20, headline, '#' * 20,"\n")


if __name__ == "__main__":
    text = read_file('input.txt')

    # a.Tokenization
    put_headline("Tokenization")
    stoken, wtoken = tokenize(text)
    print("Here are the first 4 sentences: ")
    print("\n".join(stoken[:4]))
    print()
    print("Here are the first 4 words:")
    print('\n'.join(wtoken[:4]))

    # b. POS
    put_headline("POS")
    part_of_speech = pos_tag(wtoken[:4])
    print(part_of_speech)

    # c. Stemming
    put_headline("Stemming")
    stemmer = stem(wtoken[:4])
    mapped = zip(wtoken[:4],stemmer)
    print(set(mapped))

    # d. Lemmatization
    put_headline("Lemmatization")
    lemma = lemmatize(wtoken[:20])
    mapped_lemma = zip(wtoken[:20], lemma)
    print(set(mapped_lemma))

    # e.Trigram
    put_headline("Trigram")
    trigram_dict = trigram(stoken[:4])
    for key, value in trigram_dict.items():
        print(key, value)

    # f.Named Entity Recognition
    put_headline("Named Entity Recognition")
    ner_dict  = ner(stoken[:4])
    for key, value in ner_dict.items():
        print(key, value)
        print()

