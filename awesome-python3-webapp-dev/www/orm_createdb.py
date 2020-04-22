#_coding:utf-8_
author = "toby"

import time
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/clc", encoding="utf-8", echo=True)

Base = declarative_base() #生成ORM基类

#定义一个类Host，一个表对应一个类，且这个类和表做了映射关系
class Host(Base):
    __tablename__ = "hostinfo1" #表名
    id = Column(Integer, primary_key=True) #字段
    hostname = Column(String(32)) #字段
    ip = Column(String(64)) #字段

class Use(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(64))
    passwd = Column(String(64))
    admin = Column(Boolean)
    name = Column(String(64))
    image = Column(String(600))
    created_at = Column(Float, default=time.time)

Base.metadata.create_all(engine) #创建表结构

# Session_class = sessionmaker(bind=engine) # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
# Session = Session_class() # 生成session实例
#
#
# user_obj = Host(hostname="pc1", ip="192.168.1.3") # 生成你要创建的数据对象 (这里的hostname和ip是表里的字段)
# print('--------------1--------------', user_obj.hostname, user_obj.ip, user_obj.id) # 打印数据， 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj) # 把要创建的数据对象添加到这个session里， 一会统一创建
# print('--------------2--------------', user_obj.hostname, user_obj.ip, user_obj.id) # 此时也依然还没创建
#
# Session.commit() # 现此才统一提交，创建数据
