"""
    Functions to handle pokemons
"""
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils import pokeapi

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/randomPoke")
def get_3_random_pokemons():
    """
        Return 3 random pokemons
    """
    return pokeapi.get_random_pokemons(3)

@router.get("/battle/{pokemon_a}/{pokemon_b}")
def get_battle_result(pokemon_a: int, pokemon_b: int):
    """
        Return the pokemon who win
    """
    return pokeapi.battle_pokemon(pokemon_a, pokemon_b)
