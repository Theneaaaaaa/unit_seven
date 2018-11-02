# Thenea Sun
# Oct. 11th
# This program is a encoding and decoding program which could do spy works (im joking lol),It takes in a plain-text
# string, and translates it into a new string based on a rotation of the alphabet being used. The basis is a “rotation”,
# a re-sequencing of an alphabet.


def main():
    characters = "abcdefghijklmnopqstuvwxyz"
    while True:
        codes = input("Please enter 'e' to encode."
                      "'d' to decode."
                      "'q' to quit.")
        if codes == "e":
            text = input("Please enter the text to be encoded:")
            rotation = int(input("Please enter the key (0-25):"))
            # if it is not integers, the program will not run at all.
            text = text.lower()
            first = characters[0:rotation]
            last = characters[rotation:25]
            characters1 = last + first
            # This is the new alphabet of the letter
            blank_string = ""
            for x in text:
                if x in characters:
                    pos = characters.index(x)
                    new_text = characters1[pos]
                    blank_string = blank_string + new_text
                else:
                    blank_string = blank_string + x
            print(blank_string)
        elif codes == "d":
            text = input("Please enter the text to be decoded:")
            rotation = int(input("Please enter your key:"))
            text = text.lower()
            first = characters[0:rotation]
            last = characters[rotation:25]
            characters2 = first + last
            text = text.lower()
            first = characters[0:rotation]
            last = characters[rotation:25]
            characters3 = last + first
            # This is the new alphabet of the letter
            blank_string = ""
            for x in text:
                if x in characters:
                    pos = characters3.index(x)
                    new_text = characters2[pos]
                    blank_string = blank_string + new_text
                else:
                    blank_string = blank_string + x
            print(blank_string)
            # Do the first if backwards, and then give out the original sentence
        elif codes == "q":
            print("Thank you for using this program.")
            break
        else:
            print("ERROR. Please follow the instruction.")


main()

