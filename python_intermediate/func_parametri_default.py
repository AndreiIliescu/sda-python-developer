# Default parameters.
def show_message(message="default message"):
    print(f"My message is {message}")


# Functia "show_message()" are pentru parametrul "message" are o valoare default.
# Daca apelam functia fara a specifica valori noi
# ea va folosi valoarea default.
show_message()

# Daca apelam functia cu alta valoare, ea va inlocui valoarea default.
show_message("alt mesaj")
