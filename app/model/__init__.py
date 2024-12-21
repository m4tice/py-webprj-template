from .model import DBModel
from .operator import Operator

DATABASE_OPERATOR = 'app/model/dbs/operators2.db'

model_operator = DBModel(DATABASE_OPERATOR)
data_operators = model_operator.get_all_items()

print(model_operator.get_headers())

operators = [Operator(*item) for item in data_operators]
dummy_operators = [Operator(*item) for item in data_operators[:2]]


DATABASE_WEAPONS = 'app/model/dbs/weapons.db'
model_weapon = DBModel(DATABASE_WEAPONS)
headers_weapon = model_weapon.get_headers()
data_weapons = model_weapon.get_all_items()
