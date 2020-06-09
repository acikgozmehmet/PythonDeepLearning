def change_word(sentence, word="python"):
    return sentence.replace(word, "pythons")

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    new_sentence = change_word(text)
    print(f"New sentence: {new_sentence}")