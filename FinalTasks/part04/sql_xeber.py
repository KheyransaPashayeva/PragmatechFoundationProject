from sqlalchemy_sample import session, Xeber
from sqlalchemy import func
my_date=Field(DateTime())
table_db = Xeber.query.filter(func.DATE(Xeber.date_bd) == my_date)
q = session.query(Xeber).offset(table_db).limit(10)
for xeber in q:
    print(xeber)