# 导入:
from flask import current_app, app, g
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

def getDb():
    if 'db' not in g:
        # 初始化数据库连接:
        engine = create_engine(current_app.config['DATABASE'], convert_unicode=True)
        # 创建DBSession类型:
        g.db = sessionmaker(bind=engine)
    return g.db

# # 初始化数据库连接:
# engine = create_engine(current_app.config['DATABASE'], convert_unicode=True)
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

