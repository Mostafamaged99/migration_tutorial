from settings import Setting as st
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pymysql

db_connection = f"mysql+pymysql://{st.db_user}:{st.db_pass}@{st.db_host}/{st.db_name}?charset=utf8mb4"
engine = create_engine(db_connection, echo=True)
Base = declarative_base()
