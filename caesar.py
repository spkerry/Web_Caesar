def encrypt(text, rot):
    newString = ""
    for i in range(len(text)):
        newString += rotate_character(text[i], int(rot))
    return newString

def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return i

def rotate_character(char, rot):
    rot = rot % 26
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in lower_alpha:
        x = (alphabet_position(char) + rot) % 26
        return lower_alpha[x]
    elif char in upper_alpha:
        x = (alphabet_position(char) + rot) % 26
        return upper_alpha[x]
    else:
        return char
