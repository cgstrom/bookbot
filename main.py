def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        word_count(file_contents)

def word_count(file_contents):
    count = 0
    words = file_contents.split()
    #print(words)
    for word in words:
        count += 1
    print(count)



main()