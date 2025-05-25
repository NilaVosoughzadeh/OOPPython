from orm.database import Database
from orm.fields import Field


class BaseModel:
    table_name = ''

    def __init__(self, **kwargs):
        for field_name in self.__class__.__dict__:
            if isinstance(self.__class__.__dict__[field_name], Field):
                setattr(self, field_name, kwargs.get(field_name))

    @classmethod
    def create_table(cls):
        fields = []
        for name, field in cls.__dict__.items():
            if isinstance(field, Field):
                sql = f"{name} {field.get_sql()}"
                fields.append(sql)
        fields_sql = ', '.join(fields)
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({fields_sql});"
        Database.execute(query)

    def save(self):
        fields = []
        values = []
        placeholders = []
        for name, field in self.__class__.__dict__.items():
            if isinstance(field, Field):
                value = getattr(self, name, None)

                #اعتبارسنجی
                field.validate(value)

                fields.append(name)
                fields.append(value)
                placeholders.append("?")

        if getattr(self, 'id', None):  
            set_clause = ', '.join(f"{f}=?" for f in fields if f != 'id')
            values_update = [getattr(self, f) for f in fields if f != 'id']
            values_update.append(self.id)
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
            Database.execute(query, values_update)
        else: 
            query = f"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(placeholders)})"
            Database.execute(query, values)
            self.id = Database._cursor.lastrowid

    def delete(self):
        if getattr(self, 'id', None):
            query = f"DELETE FROM {self.table_name} WHERE id = ?"
            Database.execute(query, [self.id])

    @classmethod
    def get(cls, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        where_clause = ' AND '.join(conditions)
        query = f"SELECT * FROM {cls.table_name} WHERE {where_clause} LIMIT 1"
        cursor = Database.execute(query, values)
        row = cursor.fetchone()
        if row:
            columns = [f for f in cls.__dict__ if isinstance(cls.__dict__[f], Field)]
            data = dict(zip(columns, row))
            return cls(**data)
        return None