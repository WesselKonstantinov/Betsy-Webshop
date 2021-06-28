import peewee

DATABASE = 'betsy_webshop.db'

db = peewee.SqliteDatabase(DATABASE)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class BillingInformation(BaseModel):
    card_number = peewee.IntegerField(
        unique=True,
        # Make sure card number consists of 16 digits.
        constraints=[peewee.Check('length(cast(card_number as text)) == 16')]
    )
    card_holder_name = peewee.CharField(unique=True)
    card_security_code = peewee.IntegerField(
        constraints=[peewee.Check(
            # Make sure security code consists of 3 digits.
            'length(cast(card_security_code as text)) == 3')]
    )
    expiry_month = peewee.IntegerField(
        # Make sure the selected month  is bewtween 1 and 12.
        constraints=[peewee.Check('1 <= expiry_month and expiry_month <= 12')]
    )
    expiry_year = peewee.IntegerField()
    billing_address = peewee.CharField()


class User(BaseModel):
    name = peewee.CharField()
    address = peewee.CharField()
    billing_information = peewee.ForeignKeyField(
        BillingInformation,
        unique=True
    )


class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.TextField()
    unit_price = peewee.DecimalField(max_digits=7, decimal_places=2)
    user = peewee.ForeignKeyField(User, backref='products')
    quantity = peewee.IntegerField()


class Tag(BaseModel):
    title = peewee.CharField(unique=True)
    products = peewee.ManyToManyField(Product, backref='tags')


ProductTag = Tag.products.get_through_model()


class Purchase(BaseModel):
    buyer = peewee.ForeignKeyField(User)
    bought_product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()
    transaction_date = peewee.DateTimeField()
