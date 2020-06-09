import sys
from random import randint


def pick_indices_to_delete(word):
    '''
	Given a word, it determines the index of the characters to delete randomly
	:return: a set of indices to delete, at least 2 characters up to half of the characters
	'''

    if len(word) <= 2:
        print("The length of the word must be greater than 2")
        sys.exit(1)

    count = randint(2, round(len(word) / 2))

    myset = set([])
    while len(myset) != count:
        value = randint(0, len(word) - 1)
        myset.add(value)

    return myset


def delete_characters_from_word(word, indices_to_delete):
    '''
	Given a word, deletes the characters located at indices and returns the new word
	:param word: original word
	:param indices_to_delete: the indices to delete
	:return: newly created word
	'''
    new_word = ""
    for index, letter in enumerate(word):
        if index not in indices_to_delete:
            new_word += letter
    return new_word


def reverse_the_word(word):
    '''
	Returns the reversed word
	:param word: original word
	:return: reversed word
	'''
    return word[::-1]


if __name__ == "__main__":
    word = input("Enter a word:  ")
    print(f"original word:  {word}")

    indices_to_delete = pick_indices_to_delete(word)
    print(f"indices {indices_to_delete} will be deleted from the word")

    new_word = delete_characters_from_word(word, indices_to_delete)
    print(f'new word:  {new_word}')
    print('Reversed new word: ', reverse_the_word(new_word))
