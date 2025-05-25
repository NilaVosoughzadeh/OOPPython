from orm.base_model import BaseModel
from orm.fields import IntegerField, CharField

class User(BaseModel):
    table_name = 'users'

    id = IntegerField(primary_key=True)
    name = CharField(max_length=127, null=True)
    email = CharField(max_length=255, unique=True)