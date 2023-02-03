"""
    Interfaces for Items, Pokemons and Trainers
"""
from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """
        Interface for general item
    """
    # pylint: disable=too-few-public-methods
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
        Interface for the return value of item creation request
    """
    # pylint: disable=too-few-public-methods
    pass

class Item(ItemBase):
    """
       Interface for specific item of a trainer 
    """
    # pylint: disable=too-few-public-methods
    id: int
    trainer_id: int

    class Config:
        """
            Store config of an item
        """
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """
        Interface for general pokemon
    """
    # pylint: disable=too-few-public-methods
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """"
        Interface for the return value of pokemon, request
    """
    # pylint: disable=too-few-public-methods

class Pokemon(PokemonBase):
    """"
        Interface for specific pokemon of a trainer
    """
    # pylint: disable=too-few-public-methods
    id: int
    name: str
    trainer_id: int

    class Config:
        """
            Store config of a pokemon
        """
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """"
        Interface for general trainers
    """
    # pylint: disable=too-few-public-methods
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """"
        Interface used for the trainer creation
    """
    # pylint: disable=too-few-public-methods

class Trainer(TrainerBase):
    """"
        Interface used to see stats of a trainer
    """
    # pylint: disable=too-few-public-methods
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """
            Store the config of a trainer
        """
        orm_mode = True
