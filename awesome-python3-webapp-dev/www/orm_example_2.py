from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def create_app(): #在其他地方封装的
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/clc?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

app = create_app()

# 为了避免和创建表的db产生冲突, 创建专门用于数据操作的SQLAlchemy对象
model_db = SQLAlchemy(app)


class User(model_db.Model):  # db.Model主要用于数据的增删改查, 构建表交给db.Table去完成
    __tablename__ = 'user_basic'
    # 由于模型不用于建表, 所以类型不需要设置的很严谨, 并可以省略大部分字段细节(除了default参数)
    user_id = model_db.Column(model_db.Integer, primary_key=True)
    status = model_db.Column(model_db.Integer, default=1)
    mobile = model_db.Column(model_db.String(11))
    create_time = model_db.Column(model_db.DateTime, default=datetime.now)
    update_time = model_db.Column(model_db.DateTime, default=datetime.now)


@app.route('/')
def index():
    user1 = User()
    user1.mobile = '1891111111'
    model_db.session.add(user1)
    model_db.session.commit()
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)