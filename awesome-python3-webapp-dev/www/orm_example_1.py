from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TINYINT, BIGINT, VARCHAR, CHAR, DATETIME, INTEGER
from orm_example_2 import create_app
from flask_migrate import Migrate

app = create_app()
# 创建数据库连接对象
db = SQLAlchemy(app)

# 初始化迁移器
Migrate(app, db)

# 构建表
t_user = db.Table('user_basic',
                  db.Column('user_id', BIGINT(10, unsigned=True), nullable=False, primary_key=True, autoincrement=True, comment='主键'),
                  db.Column('status', TINYINT(1), nullable=False, default=1, comment="状态"),
                  # db.Column('status1', TINYINT(1), nullable=False, default=1, comment="状态1"),
                  db.Column('mobile', CHAR(11), nullable=False, unique=True, comment='手机号'),
                  db.Column('create_time', DATETIME, nullable=False, default=datetime.now, comment='创建时间'),
                  db.Column('update_time', DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间'),
                  # 注意: 如果有外键, 定义方式和普通字段一样, 可以添加索引提高性能
                  # db.Column('leader_id', BIGINT(10, unsigned=True), default=0, comment='上级的id', index=True),
                  mysql_engine='MyISAM',
                  mysql_charset='utf8mb4')


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    # pass