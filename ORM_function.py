from sqlalchemy import create_engine, MetaData, Column, Table, ForeignKey, Integer, String, DateTime
import uuid


def AddNewMachine(name, comments):
    engine = create_engine("sqlite:///machines.db")
    metadata = MetaData(bind=engine)
    machine_table = Table('machines_names', metadata, Column('UUID', String(200), nullable=False, primary_key=True),
                          Column('name', String(200), nullable=False),
                          Column('comments', String(500), nullable=True))
    metadata.create_all()
    ins = machine_table.insert().values(UUID=str(uuid.uuid4()), name=str(name), comments=str(comments))
    conn = engine.connect()
    conn.execute(ins)
    return True


def ListAllMachine():
    engine = create_engine("sqlite:///machines.db")
    result = engine.execute('SELECT * FROM machines_names')
    result = result.fetchall()
    return result


def AddNewRepair(name, dateFrom, dateTo, comments):
    engine = create_engine("sqlite:///machines.db")
    metadata = MetaData(bind=engine)
    machine_table = Table('repairs', metadata, Column('UUID', String(200), nullable=False, primary_key=True),
                          Column('name', String(200), nullable=False),
                          Column('date_from', String(10), nullable=False),
                          Column('date_to', String(10), nullable=False),
                          Column('comments', String(5000), nullable=True))
    metadata.create_all()
    ins = machine_table.insert().values(UUID=str(uuid.uuid4()), name=str(name), date_from=dateFrom,
                                        date_to=dateTo, comments=str(comments))
    conn = engine.connect()
    conn.execute(ins)
    return True



