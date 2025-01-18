from peewee import *
import peewee
import os

os.makedirs("assets", exist_ok=True)


database = SqliteDatabase('assets/documents.db')

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Document(BaseModel):
   id=IntegerField(primary_key=True)
   ano = CharField()
   unidadegestora = CharField()
   numeracao = CharField()
   assunto = TextField()
   tipoprocesso = TextField()
   locprocesso = TextField()
#    ano = TextField()
#    address = TextField()
#    phone = IntegerField()
#    class Meta:
#       database=db
#       db_table='Documents'


try:
    database.create_tables([Document])
except Exception as e:
    print(e)
