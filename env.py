from dependencies.env_dependencies import *

engine = create_engine("mysql+pymysql://ENV_USER:ENV_PASS/ENV_TABLE?charset=utf8mb4", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()