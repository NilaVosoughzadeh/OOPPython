class Field:
    def __init__(self, field_type, primary_key=False, unique=False, default=None, null=False):
        self.field_type = field_type
        self.primary_key = primary_key
        self.unique = unique
        self.default = default
        self.null = null

    def get_sql(self):
        sql = self.field_type
        if self.primary_key:
            sql += " PRIMARY KEY"
        if self.unique:
            sql += " UNIQUE"
        if self.default is not None:
            sql += f" DEFAULT '{self.default}'"
        if not self.null:
            sql += " NOT NULL"
        return sql
    
    def validate(self, value):
        if not self.null and value is None:
            raise ValueError(f"این فیلد نمی تواند خالی باشد")


class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__('INTEGER', **kwargs)


class CharField(Field):
    def __init__(self, max_length=255, **kwargs):
        self.max_length = max_length
        super().__init__(f'VARCHAR({max_length})', **kwargs)

    def validate(self, value):
        super().validate(value)
        if value is not None and len(value) > self.max_length:
            raise ValueError(f"مقدار از طول مجاز بیشتر است ({self.max_length})")