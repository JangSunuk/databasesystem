import pandas as pd
import os

from model import *
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
engine = create_engine('')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

data_dir = ['population.csv']
a = 0



for file_path in data_dir:
    data = pd.read_csv('C:/workspace/telegram-bot/{}'.format(file_path), keep_default_na=False, encoding="cp949", header=None)
    print(len(data))
    for a in range(1, len(data)):
        seoul = Seoul(
            data.loc[a][5],
            data.loc[a][2],
            data.loc[a][3],
            data.loc[a][4],
            data.loc[a][1],
            data.loc[a][0]
            )
        session.add(seoul)
        session.commit()



session.close()
