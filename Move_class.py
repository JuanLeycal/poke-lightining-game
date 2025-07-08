import asyncio
from datetime import timedelta
import time
import aiohttp
import httpx
from pydantic import BaseModel

class Move(BaseModel):
    name: str
    type: str
    type_attack: str


    def correct_name(self):
        name = self.name.title()
        name = name.replace("-", " ")
        if '  Physical' in name or '  Special' in name:
            name = name.replace('  Physical', '')
            name = name.replace('  Special', '')
        self.name = name
    


def parse_move(move_data: dict) -> Move:
    return Move(name=move_data['name'], type=move_data["type"]["name"],type_attack=move_data["damage_class"]["name"])

async def get_move(session, move_id):
    url = f"https://pokeapi.co/api/v2/move/{move_id}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                name = data["name"]
                move_type = data["type"]["name"]
                #return Move(name, move_type)
                return data
            else:
                print(f"ID {move_id} no válido (HTTP {response.status})")
                return None
    except Exception as e:
        print(f"Error en ID {move_id}: {e}")
        return None
        
async def get_all(*ids: str):

    base = []
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_move(session,id)) for id in ids]
        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            move = parse_move(result)
            if move.type_attack != 'status':
                base.append(move)
            #print(f"{move.name} es un movimiento de tipo {move.type} de categoría {move.type_attack}")
        else:
            continue

    for i in base:
        i.correct_name()

    return base


