from time import sleep


def generator():
    letters = ('A', 'B')
    for letter in letters:
        yield letter

letters_gen = generator()

print(letters_gen.__next__())
sleep(1)
print(letters_gen.__next__())
