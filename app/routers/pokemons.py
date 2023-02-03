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

@router.get("/battle/{pokemon_a}/{pokemon_b}")
def get_pokemons(pokemon_a: int, pokemon_b: int, database: Session = Depends(get_db)):
    """
        Return the pokemon who win
    """
    return pokeapi.battle_pokemon(pokemon_a, pokemon_b)

