# Thenea Sun
# Oct. 11th
# This program is a encoding and decoding program which could do spy works (im joking lol),It takes in a plain-text
# string, and translates it into a new string based on a rotation of the alphabet being used. The basis is a “rotation”,
# a re-sequencing of an alphabet.


def main():
    characters = "abcdefghijklmnopqstuvwxyz"
    codes = input("Please enter 'e' to encode."
                  "'d' to decode."
                  "'q' to quit.")
    if codes == "e":
        text = input("Please enter the text to be encoded:")
        rotation = int(input("Please enter the key (0-25):"))
        # if it is not integers, the program will not run at all.
        lowercase_text = text.lower()
        new_characters = characters
        first = characters[0:rotation]
        last = characters[rotation:25]
        characters1 = first + last
        blank_string = ""
        for x in characters:
            if x == text:
                index = characters.index(lowercase_text)
                print(index)

main()

