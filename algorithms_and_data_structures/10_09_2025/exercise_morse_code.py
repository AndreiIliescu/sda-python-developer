### Morse Code ###

# Codul Morse:
# Alfabetul Morse codifica fiecare caracter ca o serie de puncte (.) si linii (-)
# A = .-
# Q = --.-
# 1 = .----
# Codul Morse nu tine cont de majuscule sau minuscule (se folosesc litere mari)
# Un spatiu separa literele
# Trei spatii separa cuvintele
# ex.: HEY JUDE = .... . -.-- .--- ..- -.. .
# ex.: SOS = ...---...

# Cerinta: Scrie o functie "decode_morse(morse_code: str) -> str" care:
## primeste un sir de caractere scris in cod Morse
## il decodifica intr-un string lizibil de caractere
## elimina spatiile inutile de la inceput si sfarsit

### Algoritm:
# 1. Start
# 2. Curatam spetiile inutile, folosind "strip()"
# 3. Initializarea unei liste pt. cuvinte
# 4. Impartim sirul in cuvinte Morse -> fiecare "cuvant" Morse separat
# 5. Impartim cuvantul in litere (in fiecare cuvant un spatiu separa literele)
# 6. Adaugam cuvantul in lista finala
# 7. Reconstrum fraza finala
# 8. End

### Implementarea algoritmului in cod Python
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
              }
# print(MORSE_CODE)

# Decode Morse Code
def decode_morse(morse_sequence: str) -> str:
    morse_sequence = morse_sequence.strip()
    words = []

    for morse_word in morse_sequence.split("   "): # impartim sirul morse in cuvinte, folosind tre spatii ca separator
        word = "".join(MORSE_CODE.get(morse_char, "") for morse_char in morse_word.split(" "))
        if word:
            words.append(word)

    return " ".join(words)


print(decode_morse(".... . -.--   .--- ..- -.. . -.-.--")) # 2 cuvinte, primul are 3 litere si al doilea cuvant are 4 cuvinte
print(decode_morse("...---... -.-.--"))
print(decode_morse("."))

print()

# Vrem sa facem functia inversa, din text sa ne converteasca in cod Morse
# Functia "encode_morse(text: str) -> str"

TEXT_TOMORSE = {v:k for  k, v in MORSE_CODE.items()}
# print(TEXT_TOMORSE)

# Encode Morse Code
def encode_morse(text: str) -> str:
    text = text.upper() # Codul Morse nu este case-sensitive
    words = text.split(" ") # Impartim in cuvinte
    morse_words = []

    for word in words:
        morse_chars = []
        for char in word:
            morse_code = TEXT_TOMORSE.get(char, "")
            if morse_code:
                morse_chars.append(morse_code)
        morse_words.append(" ".join(morse_chars))

    return "   ".join(morse_words)


print(encode_morse("HEY JUDE!"))
print(encode_morse("SOS!"))
print(encode_morse("Python"))
print(encode_morse("Python is a great programming language"))
