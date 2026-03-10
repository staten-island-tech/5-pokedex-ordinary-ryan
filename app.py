import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)



# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for index, mon in enumerate(data):
    print(index, ":", mon["name"]['english'])
# Add a language choice feature and print the pokemons name based on the user input
language = input("Choose a language")
for mon in pokemon:
    
print(data[0])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

""" Highest_HP = 0
for mon in pokemon:
    if mon['base']['HP'] > Highest_HP:
        Highest_HP = mon['base']['HP']
    print(Highest_HP) """
    