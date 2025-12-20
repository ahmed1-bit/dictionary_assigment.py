#Frank_Tiv

tiv_dict = {
    "sun": "Tar",
    "moon": "Ishima",
    "star": "Ishav",
    "sky": "Aondo",
    "earth": "Takur",
    "fire": "Usha",
    "rain": "Ishor",
    "wind": "Ishugh",
    "tree": "Ityav",
    "leaf": "Ikyer",
    "river": "Mnger",
    "mountain": "Tsen",
    "stone": "Ishin",
    "fish": "Ikpough",
    "bird": "Iveren",
    "dog": "Igbaan",
    "cow": "Ityer",
    "friend": "Mngerem",
    "love": "Udedoo",
    "peace": "Ushor"
}

word = input("Welcome to Tiv Dictionary! Please enter a word: ")

word = word.strip().lower()

if word in tiv_dict:
    print(f"The meaning in Tiv is: {tiv_dict[word]}")
else:
    print("Word not found in Tiv Dictionary")