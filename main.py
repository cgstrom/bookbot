def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        word_count = get_word_count(file_contents)

        letter_count = get_letter_count(file_contents)

        report = make_report(word_count, letter_count)

        print(word_count)
        print(letter_count)
        print(report)

def get_word_count(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def get_letter_count(file_contents):

    char_count = {}

    file_contents = file_contents.lower()
    #print(file_contents)

    for letter in file_contents:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    return char_count

    """
    sorted_character_counts = dict(sorted(char_count.items()))

    for char, count in sorted_character_counts.items():
        print(f"'{char}': {count}")

    print(sorted_character_counts)
    """

def make_report(word_count, letter_count):
    report = "--- Begin report of books/frankenstein.txt ---"
    report = report + f"\n{word_count} words found in document"

    

    return report



main()