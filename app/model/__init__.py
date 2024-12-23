from .model import DBModel
from .operator import Operator

DATABASE_OPERATOR = 'app/model/dbs/operators2.db'

model_operator = DBModel(DATABASE_OPERATOR)
data_operators = model_operator.get_all_items()

print(model_operator.get_headers())

operators = [Operator(*item) for item in data_operators]
data_operators_dummy = [data_operators[0],
                        data_operators[3],
                        data_operators[7],
                        data_operators[14],
                        data_operators[19],
                        data_operators[28],
                        data_operators[30],
                        data_operators[32],
                        data_operators[35]]
dummy_operators = [Operator(*item) for item in data_operators_dummy]


DATABASE_WEAPONS = 'app/model/dbs/weapons.db'
model_weapon = DBModel(DATABASE_WEAPONS)
headers_weapon = model_weapon.get_headers()
data_weapons = model_weapon.get_all_items()[:10]
