def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = get_word_count(file_contents)

        letter_count = get_letter_count(file_contents)

        report = make_report(word_count, letter_count)

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

    for letter in file_contents:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    return char_count

def make_report(word_count, letter_count):

    letter_count_list = []

    for letter in letter_count:
        letter_dict = {}
        if letter.isalpha() == True:
            letter_dict["char"] = letter
            letter_dict["count"] = letter_count[letter]
            letter_count_list.append(letter_dict)

    def sort_on(dict):
        return dict["count"]

    letter_count_list.sort(reverse = True, key = sort_on)

    report = "\n--- Begin report of books/frankenstein.txt ---"
    report = report + f"\n{word_count} words found in document\n"

    for i in letter_count_list:
        report += f"\nThe '{i["char"]}' character was found {i["count"]} times"

    report += "\n--- End report ---\n"

    return report



main()