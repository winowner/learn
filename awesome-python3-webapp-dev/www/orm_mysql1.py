import  pymysql
class  Field:
    def __init__(self,name,column=None,pk=False,unique=False,index=False,nullable=True,default=None):
        self.name=name  # 字段名称
        if  column  is None:  #列名称
            self.column=self.name
        else:
            self.column=column
        self.pk=pk  # 主键
        self.unique=unique  #唯一
        self.index=index #索引
        self.nullable=nullable  #是否为空
        self.default=default  # 默认是否为空
    def  validate(self,value):  # 此处定义数据校验方式，每种不同类型的校验方式不同，因此应该在子类中分别实现
        raise  NotImplementedError  #基类不实现此功能

    def __get__(self, instance, owner): #此处用于定义描述器，此处当子类的类调用此属性时，会返回对应的值
        # 此处的self表示父类的实例，instance表示子类的实例，owner表示子类的类
        # pass
        if instance is None:  #此处为None表示子类未生成对应实例
            return self  # 此处的self表示实例自己
        return  instance.__dict__[self.name]  # 返回实例对应的字段名称
    def __set__(self, instance, value): #此处用于定义数据描述器，用于子类实例调用时使用，用于返回对应的结果
        # instace 表示子类的实例，其相关的信息应该被存储于子类实例中，
        self.validate(value)
        instance.__dict__[self.name]=value #此处的name是字段名，value是子类的self,对应的属性的值，及真实的数据

    def  __str__(self):
        return   "{} <{}>".format(self.__class__.__name__,self.name)  # 此处返回被调用的类名和实例名称
    __repr__=__str__
# 定义整数类型的类型属性
class  IntField(Field):  #多了自增属性。
    def  __init__(self,name=None,column=None,pk=False,unique=False,index=False,nullable=True,default=None,auto_increment=True):
        self.auto_increment=auto_increment
        super().__init__(name,column,pk,unique,index,nullable,default)

    def validate(self,value):
        if value is  None:
            if self.pk:  # 主键不能为空，因此此处会报错
                raise TypeError("{}:{}".format(self.name,value))
            if not self.nullable:  # 当定义了非空时，上述的值为空，则报错
                raise TypeError
        else:
            if not isinstance(value,int):  #若数据的类型为非int，则报错
                raise TypeError("{}  is  not  int,  It's {}".format(self.name,type(value)))

# 定义字符串的类型属性
class  StringField(Field):  #定义字符串属性类
    # 增加了字符串长度的定义
    def __init__(self,length=32,name=None,column=None,pk=False,unique=False,index=False,nullable=True,default=None):
        super().__init__(name,column,pk,unique,index,nullable,default)  #此处的属性可以继承父类的属性
        self.length=length  #此处用于定义字符串类型的长度
    def  validate(self,value):  #此处用于定义各自的属性检查,对数据进行属性检查
        if  value  is None: # 此处的None对应数据库的null
            if self.pk:  # 如果数据是None，而其定义了主键，则会报错，因为主键必须不能是Null，主键非空且唯一
                raise TypeError("{} is pk,not None".format(self.name))
            if not  self.nullable:  # 如果其是None,而定义的是非null，则会报错
                raise TypeError("{}  is  not  null".format(self.name))
        else:
            if not isinstance(value,str):
                raise TypeError("{} should be string".format(self.name))
            if len(value) > self.length:  #真实的值大于规定的值，则会报错
                raise ValueError("{} is to long value={}".format(self.name,value))

# 具体类的实现
class  Session:  #此处用以封装链接，可在此处增加上下文支持
    def __init__(self,conn:pymysql.connections.Connection):
        self.conn=conn
        self.cursor=None

    def execute(self,query,*args):
        if self.cursor is None:
            self.cursor=self.conn.cursor()
        self.cursor.execute(query,*args)
    def __enter__(self): # 此处实现方式和
        return self.conn.cursor()
        # self.cursor=self.conn.cursor()
        # return self 如此写，这个session必须是一个线程级别的，如果用进程，则直接覆盖cursor
        # 因为线程是顺序执行的，都用新的cursor（）当查询数据时，数据找不到了，因为cursor变了。本session是在线程内执行，不能夸线程执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if exc_type: # 此处用于定义是否出错，若出错，则直接返回
            self.conn.rollback()
        else:
            self.conn.commit()

class ModeMetd(type):  # 子类构建的时候实现的
    def __new__(cls,name,bases,attrs:dict):  # 此处是在类的定义中进行调用的，
        # 此处的name表示被调用子类的类名，而对应的字典attrs则表示子类的属性字典
        # name 类名，attrs类属性字典
        if '__table__'  not in attrs.keys():
            attrs['__table__']=name   #默认添加表名称为类名称

        mapping={}  # 方便后面查询属性名和字段实例
        primarykey=[]  # 多个主键的情况下使用，如果使用一个变量名，则导致后面覆盖前面
        for k,v in attrs.items():  # k代表的是列名称，v表示的是子类的类型
            if isinstance(v,Field):  # 此处判断是否继承与父类
                mapping[k]=v
                if  v.name is None:
                    v.name=k  # 如果是，则将类.name
                if  v.column is None:
                    v.column=v.name # 没有给字段名,则使用类对应的列名称
                if v.pk:
                    primarykey.append(v)
        # 增加属性
        attrs['__mapping__']=mapping
        attrs['__primarykey__']=primarykey
        return super().__new__(cls,name,bases,attrs)

class  Model(metaclass=ModeMetd):  # 实体类的调用时实现，子类的实例调用时实现的
    def save(self, session: Session = None):
        names = []
        values = []
        for k, v in self.__class__.__dict__.items():  # 此处用于获取实例的名称和其对应的值
            # print ('for',k,'---',v)
            if isinstance(v, Field):  # 此处若属于基类
                if k in self.__dict__.keys():  # 此处的字段符合
                    names.append(k)
                    values.append(self.__dict__[k])  # v是一个Field类型的实例，是子类和父类的实例
                    print(self.__dict__[k])  # 此处是实例。实例中的数字
        # __table__  # 此处在子类中添加
        query = "insert into {} ({}) values ({})".format(self.__table__, ",".join(names),
                                                         ",".join(["%s"] * len(values)))  # 此处是匹配对应的sql
        print(query)
        # with  session:
        #     session.execute(query,values)

class  Login(Model):
    id=IntField(pk=True,nullable=False,auto_increment=True)
    name=StringField(length=64,nullable=False)
    age=IntField()
    __table__='login'
    def  __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def __str__(self):
        return   "Loin({},{},{})".format(self.id,self.name,self.age)
    __repr__=__str__
class  Engine:
    def __init__(self,*args,**kwargs):
        self.conn=pymysql.connections.Connection(*args,**kwargs)
    def save(self, instance:Login):
        names = []
        values = []
        for k, v in instance.__mapping__.items():  # 此处用于获取实例的名称和其对应的值
            # print ('for',k,'---',v)
            if isinstance(v, Field):  # 此处若属于基类
                if k in instance.__dict__.keys():  # 此处的字段符合
                    names.append(k)
                    values.append(instance.__dict__[k])  # v是一个Field类型的实例，是子类和父类的实例
        # __table__  # 此处在子类中添加
        query = "insert into {}({}) values({})".format(instance.__table__, ",".join(names),
                                                         ",".join(["%s"] * len(values)))  # 此处是匹配对应的sql
        S=Session(self.conn)
        with  S:
            S.execute(query,values)

e=Engine('127.0.0.1','root','root','clc')
for  i in range(10):
    e.save(Login(i,'admin'+str(i),20+i))