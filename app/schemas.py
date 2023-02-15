"""
    Interfaces for Items, Pokemons and Trainers
"""
# pylint: disable=no-name-in-module
# pylint: disable=too-few-public-methods
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
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
        Interface for the return value of item creation request
    """

class Item(ItemBase):
    """
       Interface for specific item of a trainer
    """
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
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """"
        Interface for the return value of pokemon, request
    """

class Pokemon(PokemonBase):
    """"
        Interface for specific pokemon of a trainer
    """
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
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """"
        Interface used for the trainer creation
    """

class Trainer(TrainerBase):
    """"
        Interface used to see stats of a trainer
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """
            Store the config of a trainer
        """
        orm_mode = True
