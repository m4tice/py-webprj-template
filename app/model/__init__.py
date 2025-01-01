from .model import DBModel
from .operator import Operator


# Opeartor DB instance
DATABASE_OPERATOR = 'app/model/dbs/operators2.db'
model_operator = DBModel(DATABASE_OPERATOR)

# All data from the operators table
data_operators = model_operator.get_all_items()
operators = [Operator(*item) for item in data_operators]

# Dummy data from the operators table
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


# Weapon DB instance
DATABASE_WEAPONS = 'app/model/dbs/weapons.db'
model_weapon = DBModel(DATABASE_WEAPONS)

# Headers for the weapons table
headers_weapon = model_weapon.get_headers()

# Data from the weapons table
data_weapons = model_weapon.get_all_items()[:10]

# Data for card_01.html
operator_instance = Operator(*data_operators[30])


# RQ1 data
DATABASE_RQ1 = 'app/model/dbs/rq1.db'
model_rq1 = DBModel(DATABASE_RQ1)

# Headers for the RQ1 table
data_rq1 = model_rq1.get_all_items()
data_rq1_headers = model_rq1.get_headers()

packages = ['ComServices',
            'ComVeh',
            'ComCo',
            'ComPtc',
            'ComDia',
            'LinStack',
            'SENT']
