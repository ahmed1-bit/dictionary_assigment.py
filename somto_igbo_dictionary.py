# english to igbo dictionary
igbo_dictionary = {
    "water": "mmiri",
    "food": "nri",
    "house": "ulo",
    "man": "nwoke",
    "woman": "nwanyi",
    "child": "nwa",
    "eat": "rie",
    "drink": "nuo",
    "sleep": "rahu ura",
    "walk": "ga ije",
    "run": "gba oso",
    "sit": "nodu",
    "stand": "guzo",
    "come": "bla",
    "go": "gaa",
    "talk": "kwuo",
    "see": "hu",
    "hear": "nu",
    "read": "guo",
    "write": "dee",
}
print("ENGLISH -> IGBO_DICTIONARY")
print("type 'exit' to exit")
while True:
    word = input("enter an english word:").lower()
    if word == "exit":
        print("Goodbye")
        break
    if word in igbo_dictionary:
        print("igbo translation:", igbo_dictionary[word])
    else:
        print("word not recognized")