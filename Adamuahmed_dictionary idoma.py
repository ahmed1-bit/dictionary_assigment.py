# simple english to Idoma_dictionary

Idoma_dictionary = {
  "Goodmorning": "Nma ochi",
  "How are you": "Abo le",
  "Hey": "Oyi",
  "Are you okay?": "A gbe hii",
  "Welcome": "Ainya o wa",
  "Thank you": "Ainya",
  "Goodnight": "Nmo gbchi",
  "I am fine": "Mgbehi",
  "Goodafternoon": "Nma eno",
  "Goodevening": "Nma one",
  "Please": "Kocho",
  "Sorry": "Nma",
  "Hardluck": "Okwiye",
  "Today": "Inche",
  "Yesterday": "Ene",
  "Sunday": "Aladi",
  "God": "Ocho",
  "Church": "uka",
  "sacred": "iho",
  "Peace": "ebo"
}

print("English = idoma Dictionary")
print("Type 'exit' to stop\n")

while True:
  word = input("Enter an English word: ").Lower()
  
  if word == "exit":
    print("Bye ")
    break
  
  if word in dictionary:
    print("Idoma:", dictionary[word])
  else:
      print("Word not found")