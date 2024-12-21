from .model import DBModel
from .operator import Operator

DATABASE = 'app/model/dbs/operators.db'

model = DBModel(DATABASE)
data = model.get_all_items()
operators = [Operator(*item) for item in data]
dummy_operators = [Operator(*item) for item in data[:2]]
