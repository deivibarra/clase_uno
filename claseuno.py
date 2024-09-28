meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Reir a carcajadas",
}

word = input("Introduce una palabra que no entiendas (¡con Mayuscula): ")

if word in meme_dict.keys():
    print(f"La palabra {word} significa: {meme_dict[word]}")
else:
    print("No tengo esa palabra en mi diccionario")


