import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from sqlalchemy.orm import Session
from app.actions import *
from app.models import Trainer, Item
import datetime


fake_session = Mock(spec=Session)
fake_trainer = Trainer(id=1, name="John Doe")
fake_trainer2 = Trainer(id=2, name="Jane Doe")

class TestAction(unittest.TestCase):
    def test_get_trainer(self):
        fake_session.query.return_value.filter.return_value.first.return_value = fake_trainer
        
        result = get_trainer(fake_session, 1)
        
        self.assertEqual(result, fake_trainer)
    
    def test_get_trainer_by_name(self):
        fake_session.query.return_value.filter.return_value.all.return_value = [fake_trainer, fake_trainer2]
        
        result = get_trainer_by_name(fake_session, "Doe")
        
        self.assertEqual(result, [fake_trainer, fake_trainer2])

    def test_get_trainers(self):
        fake_session.query.return_value.offset.return_value.limit.return_value.all.return_value = [fake_trainer, fake_trainer2]
        
        result = get_trainers(fake_session, skip=1, limit=1)
        
        self.assertEqual(result, [fake_trainer, fake_trainer2])
    
    def test_create_trainer(self):
        fake_session = MagicMock()
        trainer = schemas.TrainerCreate(name="John Doe", birthdate="1980-01-01")

        create_trainer(fake_session, trainer)

        fake_session.add.assert_called_once()
        fake_session.commit.assert_called_once()
        trainer_arg = fake_session.add.call_args[0][0]
        self.assertEqual(trainer_arg.name, "John Doe")
        self.assertEqual(trainer_arg.birthdate, datetime.date(1980, 1, 1))
    
    def test_get_items(self):
        fake_item = Item(id=1, name="Item", description="It is an item")
        fake_session.query.return_value.offset.return_value.limit.return_value.all.return_value = fake_item
        
        result = get_items(fake_session, 1)
        
        self.assertEqual(result, fake_item)

    