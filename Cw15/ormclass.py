from conf import conn
from psycopg2.extensions import connection

class Student():


    __conn:connection = conn
    _table_name = ''


    def __init__(self,student_id:int,name:str) -> None:
        self.id = student_id
        self.name = name


    def __str__(self) -> str:
        return f'Student(id: {self.id},Name: {self.name})'
    

    @classmethod
    def create_table(cls):
        cur = cls.__conn.cursor()
        cur.execute(f"create table if not exists student(id integer, name varchar(20))")


    def save(self):
        cur = self.__conn.cursor()
        cur.execute(f"INSERT INTO public.student (id, name) VALUES ({self.id}, '{self.name}');")


    @classmethod 
    def get(cls,**kwargs):
        cursor = cls.__conn.cursor()
        q = " and ".join([f'{k}={v}'for k,v in kwargs.items() ])
        cursor.execute(f'select id,name from {cls._table_name}where {q};')
        result = cursor.fetchone()
        return cls(*result)
    


# s1 = Student(1,'mohammad')

# Student.create_table()
# s1.save()
s1 = Student.get(id = 1)
print(s1)
conn.commit()
conn.close()