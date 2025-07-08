import asyncio
import json
import Move_class as mv
import Pokemon_cass as pk

async def main():
    move_ids = list(range(1, 920))  # Rango válido
    moves = await mv.get_all(*map(str, move_ids))
    print(f"Movimientos válidos: {len(moves)}")
    print(moves)
    
    ids = list(range(1, 1026))  # Todos los Pokémon conocidos hasta Gen 9
    all_pokemon = await pk.get_all(*map(str, ids))
    print(f"Pokémon válidos: {len(all_pokemon)}")
    
asyncio.run(main())