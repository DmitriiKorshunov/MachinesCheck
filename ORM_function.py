from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
import uuid, datetime

engine = create_engine("sqlite:///machines.db")
Base = declarative_base()


class RepairTable(Base):
    __tablename__ = 'repairs'
    UUID = Column(String(200), nullable=False, primary_key=True)
    name = Column(String(200), nullable=False)
    date_from = Column(String(10), nullable=False)
    date_to = Column(String(10), nullable=False)
    comments = Column(String(5000), nullable=True)

    def __init__(self,UUID,name,date_from,date_to,comments):
        self.UUID = UUID
        self.name = name
        self.date_from = date_from
        self.date_to = date_to
        self.comments = comments


    def __repr__(self):
        return "(%s, %s, %s, %s, %s)" % (self.UUID, self.name, self.date_from, self.date_to, self.comments)


class MachineNamesTable(Base):
    __tablename__ = 'machines_names'
    UUID = Column(String(200), nullable=False, primary_key=True)
    name = Column(String(200), nullable=False)
    comments = Column(String(500), nullable=True)

    def __init__(self,UUID,name,comments):
        self.UUID = UUID
        self.name = name
        self.comments = comments


    def __repr__(self):
        return "(%s, %s, %s)" % (self.UUID, self.name, self.comments)


def ListAllMachine ():
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    result = session.query(MachineNamesTable).all()
    return result

def AddNewRepair (name, dateFrom, dateTo, comments):
    try:
        new_item = RepairTable(str(uuid.uuid4()), str(name), str(dateFrom), str(dateTo), str(comments))
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()
        session.add(new_item)
        session.commit()
        return True
    except:
        return False

def CheckExistItemsRepair (name,dateFrom, dateTo, comment):
        engine = create_engine("sqlite:///machines.db")
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()
        result = session.query(RepairTable).filter(RepairTable.name==str(name)).filter\
            (RepairTable.date_to==dateTo.strftime('%d-%m-%Y')).filter\
                (RepairTable.date_from==dateFrom.strftime('%d-%m-%Y')).filter\
                (RepairTable.comments==str(comment)).all()
        if len(result) > 0:
            # (Per. on new add , text,  addative btn, UUID)
            return (False, 'Запись уже существует!', False, False)
        result = session.query(RepairTable).filter(RepairTable.name == str(name)).all()
        for item in result:
            to_base_date = datetime.datetime(int(item.date_to.split('-')[2]),
                                         int(item.date_to.split('-')[1]),
                                         int(item.date_to.split('-')[0]))
            from_base_date = datetime.datetime(int(item.date_from.split('-')[2]),
                                         int(item.date_from.split('-')[1]),
                                         int(item.date_from.split('-')[0]))
            to_new_date = dateTo
            from_new_date = dateFrom
            if from_new_date == from_base_date:
                if to_new_date == to_base_date:
                    return (False, 'Запись о ремонте в течении данного срока'
                                   ' существует. Добавить текущие изменения?', True, item.UUID)

def DeleteRepairUUID(UUID):
        engine = create_engine("sqlite:///machines.db")
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()
        session.query(RepairTable).filter(RepairTable.UUID==UUID).delete()
        session.commit()
        print('Done')

