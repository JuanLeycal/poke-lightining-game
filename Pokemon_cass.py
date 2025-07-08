import asyncio
from datetime import timedelta
import time
import httpx
import aiohttp
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    types: list[str]
    image: str

    def correct_name(self):
        name = self.name.title()
        name = name.replace("-", " ")
        self.name = name
        
    

def parse_move(pokemon_data: dict) -> Pokemon:
    poke_types = []
    for poke_type in pokemon_data["types"]:
        poke_types.append(poke_type["type"]["name"])

    return Pokemon(name=pokemon_data['name'], types=poke_types, image=pokemon_data['sprites']['other']['official-artwork']['front_default'])

timeout = httpx.Timeout(10.0, read=None)

async def get_pokemon(session,pokemon_id: str) -> dict | None:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                name = data["name"]
                types = [t["type"]["name"] for t in data["types"]]
                image = data["sprites"]["front_default"]
                return data
            else:
                print(f"ID {pokemon_id} no válido (HTTP {response.status})")
                return None
    except Exception as e:
        print(f"Error en ID {pokemon_id}: {e}")
        return None

async def get_all(*ids: str):

    base = []

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_pokemon(session,id)) for id in ids]
        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            move = parse_move(result)
            base.append(move)
            #print(f"{move.name} es un movimiento de tipo {move.type} de categoría {move.type_attack}")
        else:
            continue

    for i in base:
        i.correct_name()

    return base