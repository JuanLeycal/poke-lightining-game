import asyncio
from datetime import timedelta
import time
import httpx
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


async def get_pokemon(id: str) -> dict | None:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 404:
                return None
            raise
        else:
            return resp.json()

async def get_all(*ids: str):

    base = []

    tasks = [asyncio.create_task(get_pokemon(id)) for id in ids]

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