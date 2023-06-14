import requests

from src.models.pokemon import Pokemon


class PokemonApiService():

    def get_pokemon(self, pokemon_name):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name).json()
        pokemon_name = response["name"]
        pokemon_types = self.get_pokemon_types(response)

        return Pokemon(pokemon_name, pokemon_types)

    def get_pokemon_types(self, response_json):
        types_array = []
        for type in response_json["types"]:
            types_array.append(type["type"]["name"])

        return types_array

    def pretty_print_pokemon(self, pokemon):
        print("Name: " + pokemon.name)
        print("Type(s): ")
        for type in pokemon.types:
            print(type)


