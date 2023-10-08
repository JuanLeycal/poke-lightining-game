import asyncio
from datetime import timedelta
import time
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

async def get_move(id: str) -> dict | None:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://pokeapi.co/api/v2/move/{id}")
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

    tasks = [asyncio.create_task(get_move(id)) for id in ids]

    results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            move = parse_move(result)
            if move.type_attack != 'status':
                base.append(move)
            #print(f"{move.name} es un movimiento de tipo {move.type} de categoría {move.type_attack}")
        else:
            print(f"No hay tipo")

    for i in base:
        i.correct_name()

    return base