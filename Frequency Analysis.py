from collections import Counter
import string


def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


def letter_frequency_analysis(text):
    cleaned_text = clean_text(text)

    letter_counts = Counter(char for char in cleaned_text if char.isalpha())

    most_common_letters = letter_counts.most_common(10)

    print("Top 10 Most Common Letters:")
    for letter, count in most_common_letters:
        print(f"{letter}: {count}")


def repeated_words_analysis(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    word_counts = Counter(words)

    repeated_words = {word: count for word, count in word_counts.items() if count > 1}

    if repeated_words:
        print("\nRepeated Words (more than once):")
        for word, count in repeated_words.items():
            print(f"{word}: {count}")
    else:
        print("\nNo words repeated more than once.")


text = input("Enter the cipher text: ")
letter_frequency_analysis(text)
repeated_words_analysis(text)
