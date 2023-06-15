from src.services.pokemon_api_service import PokemonApiService

service = PokemonApiService()
if __name__ == "__main__":
    charizard = service.get_pokemon("charizard")
    service.pretty_print_pokemon(charizard)
