import requests

from src.models.pokemon import Pokemon


class PokemonApiService:

    def get_pokemon(self, pokemon_name):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name).json()
        name = response["name"]
        types = self.get_pokemon_types(response)
        stats = self.get_base_stats(response)
        return Pokemon(name, types, stats)

    def get_pokemon_types(self, response_json):
        types_array = []
        for type in response_json["types"]:
            types_array.append(type["type"]["name"])

        return types_array

    def get_base_stats(self, response_json):
        stats = {}
        for stat in response_json["stats"]:
            stats[stat["stat"]["name"]] = stat["base_stat"]

        return stats

    def pretty_print_pokemon(self, pokemon):
        print("Name: " + pokemon.name)
        print("Type(s): ")
        for type in pokemon.types:
            print(type)

        print("Stats:")
        for stat, base_value in pokemon.stats.items():
            print(f"{stat} : {base_value}")



