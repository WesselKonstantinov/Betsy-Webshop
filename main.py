import os
import models
from datetime import datetime

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


# Functions responsible for creating and filling tables with data.
def create_tables():
    """Create tables to start using the models."""
    with models.db:
        models.db.create_tables([
            models.BillingInformation,
            models.User,
            models.Product,
            models.Tag,
            models.ProductTag,
            models.Purchase,
        ])


def fill_tables():
    """Add initial mock data (users, products and tags) to tables."""
    # Data related to user 1
    user_1_billing_info = models.BillingInformation.create(
        card_number=1234_5678_9012_3456,
        card_holder_name='J. Bierenbroodspot',
        card_security_code=456,
        expiry_month=5,
        expiry_year=2023,
        billing_address='Vikingpad 45, 1234 AB Amsterdam'
    )
    user_1 = models.User.create(
        name='Jan Bierenbroodspot',
        address='Vikingpad 45',
        billing_information=user_1_billing_info
    )

    iphone = models.Product.create(
        name='Apple Iphone',
        description='Very cool smartphone made by Apple. Almost good as new.',
        unit_price=487.99,
        user=user_1,
        quantity=1
    )

    smartphone_tag = models.Tag.create(title='smartphone')
    apple_tag = models.Tag.create(title='Apple')
    iphone_tag = models.Tag.create(title='Iphone')

    for product_tag in [smartphone_tag, apple_tag, iphone_tag]:
        product_tag.products.add(iphone)

    # Data related to user 2
    user_2_billing_info = models.BillingInformation.create(
        card_number=9987_6543_2109_8765,
        card_holder_name='L. Suikerbuik',
        card_security_code=789,
        expiry_month=1,
        expiry_year=2024,
        billing_address='Vleutenstraat 102, 1010 CT Amsterdam'
    )
    user_2 = models.User.create(
        name='Lisa Suikerbuik',
        address='Vleutenstraat 102',
        billing_information=user_2_billing_info
    )

    adidas_shoes = models.Product.create(
        name='Adidas Women\'s running shoes',
        description='These modern shoes are perfect for the city.',
        unit_price=36.00,
        user=user_2,
        quantity=2  # Denotes two pairs of shoes
    )

    shoes_tag = models.Tag.create(title='shoes')
    running_tag = models.Tag.create(title='running')
    adidas_tag = models.Tag.create(title='Adidas')

    for product_tag in [shoes_tag, running_tag, adidas_tag]:
        product_tag.products.add(adidas_shoes)

    samsung_galaxy = models.Product.create(
        name='Samsung Galaxy S21 Ultra',
        description='Sleek design. It offers very fast performance.',
        unit_price=849.99,
        user=user_2,
        quantity=1
    )

    samsung_tag = models.Tag.create(title='Samsung')
    galaxy_tag = models.Tag.create(title='Galaxy')
    android_tag = models.Tag.create(title='Android')

    for product_tag in [smartphone_tag, samsung_tag, galaxy_tag, android_tag]:
        product_tag.products.add(samsung_galaxy)

    # Data related to user 3
    user_3_billing_info = models.BillingInformation.create(
        card_number=5656_7878_3434_1212,
        card_holder_name='D. Spijkerboer',
        card_security_code=234,
        expiry_month=8,
        expiry_year=2026,
        billing_address='Slichtenhorststraat 12a, 6820 DE Arnhem'
    )
    user_3 = models.User.create(
        name='Dennis Spijkerboer',
        address='Slichtenhorststraat 12a',
        billing_information=user_3_billing_info
    )

    pinball_table = models.Product.create(
        name='Pinball table',
        description='The perfect game. Will keep you entertained for hours.',
        unit_price=255.55,
        user=user_3,
        quantity=1
    )

    pinball_tag = models.Tag.create(title='pinball')
    table_tag = models.Tag.create(title='table')
    entertainment_tag = models.Tag.create(title='entertainment')
    game_tag = models.Tag.create(title='game')

    for product_tag in [pinball_tag, table_tag, entertainment_tag, game_tag]:
        product_tag.products.add(pinball_table)

    monopoly_board_game = models.Product.create(
        name='Monopoly classic board game',
        description='The famous real estate game for quick negotiators',
        unit_price=24.95,
        user=user_3,
        quantity=3
    )

    monopoly_tag = models.Tag.create(title='Monopoly')
    board_tag = models.Tag.create(title='board')

    for product_tag in [monopoly_tag, board_tag, game_tag, entertainment_tag]:
        product_tag.products.add(monopoly_board_game)

    # Data related to user 4
    user_4_billing_info = models.BillingInformation.create(
        card_number=1111_2222_3333_4444,
        card_holder_name='E. Hakkenbrak',
        card_security_code=100,
        expiry_month=11,
        expiry_year=2025,
        billing_address='Tienraaikade 20, 5801 RF Venray'
    )
    user_4 = models.User.create(
        name='Erik Hakkenbrak',
        address='Tienraaikade 20',
        billing_information=user_4_billing_info
    )

    lego_duplo = models.Product.create(
        name='Lego Duplo set',
        description='This set consists of 4 buildable Lego Duplo vehicles.',
        unit_price=19.99,
        user=user_4,
        quantity=2
    )

    lego_tag = models.Tag.create(title='Lego')
    duplo_tag = models.Tag.create(title='Duplo')
    toys_tag = models.Tag.create(title='toys')

    for product_tag in [lego_tag, duplo_tag, toys_tag, entertainment_tag]:
        product_tag.products.add(lego_duplo)

    lego_ninjago = models.Product.create(
        name='Lego Ninjago set',
        description='Includes a jungle attack vehicle and an action figure',
        unit_price=8.99,
        user=user_4,
        quantity=1
    )

    ninjago_tag = models.Tag.create(title='Ninjago')

    for product_tag in [lego_tag, ninjago_tag, toys_tag, entertainment_tag]:
        product_tag.products.add(lego_ninjago)

    lego_disney = models.Product.create(
        name='Lego Disney princess set',
        description='A small collectible containing 157(!) pieces.',
        unit_price=39.99,
        user=user_4,
        quantity=1
    )

    disney_tag = models.Tag.create(title='Disney')
    princess_tag = models.Tag.create(title='princess')

    for product_tag in [lego_tag, disney_tag, princess_tag, toys_tag,
                        entertainment_tag]:
        product_tag.products.add(lego_disney)

    # Data related to user 5
    user_5_billing_info = models.BillingInformation.create(
        card_number=1001_2002_3003_4004,
        card_holder_name='C. Ramspek',
        card_security_code=208,
        expiry_month=10,
        expiry_year=2023,
        billing_address='Rossumplein 167, 1107 BJ Almere'
    )
    user_5 = models.User.create(
        name='Carla Ramspek',
        address='Rossumplein 167',
        billing_information=user_5_billing_info
    )

    wireless_earbuds = models.Product.create(
        name='Wireless earbuds with microphone',
        description='Uses the latest Bluetooth 5.0 technology.',
        unit_price=19.99,
        user=user_5,
        quantity=5  # Just like shoes, it denotes 5 pairs of earbuds.
    )

    wireless_tag = models.Tag.create(title='wireless')
    earbuds_tag = models.Tag.create(title='earbuds')
    microphone_tag = models.Tag.create(title='microphone')
    bluetooth_tag = models.Tag.create(title='Bluetooth')

    for product_tag in [wireless_tag, earbuds_tag, microphone_tag,
                        bluetooth_tag]:
        product_tag.products.add(wireless_earbuds)

    # Data related to user 6
    user_6_billing_info = models.BillingInformation.create(
        card_number=1357_2468_0246_9753,
        card_holder_name='N. Gietermans',
        card_security_code=304,
        expiry_month=4,
        expiry_year=2027,
        billing_address='Tolkamerstraat 5, 1703 WA Alkmaar'
    )
    user_6 = models.User.create(
        name='Nikkie Gietermans',
        address='Tolkamerstraat 5',
        billing_information=user_6_billing_info
    )

    bracelet = models.Product.create(
        name='Swarovski deluxe bracelet',
        description='This bracelet features an impressive design.',
        unit_price=127.95,
        user=user_6,
        quantity=2
    )

    jewelry_tag = models.Tag.create(title='jewelry')
    bracelet_tag = models.Tag.create(title='bracelet')
    deluxe_tag = models.Tag.create(title='deluxe')
    swarovski_tag = models.Tag.create(title='Swarovski')

    for product_tag in [jewelry_tag, bracelet_tag, deluxe_tag, swarovski_tag]:
        product_tag.products.add(bracelet)

    necklace = models.Product.create(
        name='Necklace made with Swarovski crystals',
        description='A beautiful white gold plated necklace.',
        unit_price=39.99,
        user=user_6,
        quantity=3
    )

    necklace_tag = models.Tag.create(title='necklace')
    crystal_tag = models.Tag.create(title='crystal')

    for product_tag in [jewelry_tag, necklace_tag, swarovski_tag,
                        crystal_tag]:
        product_tag.products.add(necklace)


# Functions responsible for querying the tables.
def search(term):
    """Search for products based on a given term."""
    query = models.Product.select().where(
        (models.Product.name.contains(term))
        | (models.Product.description.contains(term)))
    if query:
        print(f"\nProduct search results for the term '{term}':\n")
        for product in query:
            print(f'- {product.name} (€{product.unit_price})')
    else:
        print('Unfortunately, no products matched your search term.')


def list_user_products(user_id):
    """Display the products of a given user."""
    try:
        user = models.User.get_by_id(user_id)
    except models.User.DoesNotExist:
        print('Unfortunately, the requested user does not exist.')
    else:
        # Access user products by using the back-reference.
        if user.products:
            print(f'\nProducts offered by {user.name}:\n')
            for product in user.products:
                print(f'- {product.name} (€{product.unit_price})')
        else:
            print(f'{user.name} does not yet offer any products for sale.')


def list_products_per_tag(tag_id):
    """Display the products for a given tag."""
    try:
        tag = models.Tag.get_by_id(tag_id)
    except models.Tag.DoesNotExist:
        print('Unfortunately, the requested tag does not exist.')
    else:
        if tag.products:
            print(f"\nProducts tagged with '{tag.title}':\n")
            for product in tag.products:
                print(f'- {product.name} (€{product.unit_price})')
        else:
            print(f"There were no products found tagged with '{tag.title}'.")


def add_product_to_catalog(user_id, product):
    """Add a new product to the user's catalog."""
    try:
        user = models.User.get_by_id(user_id)
    except models.User.DoesNotExist:
        print('Unfortunately, the requested user does not exist.')
    else:
        new_product = models.Product.create(
            name=product['name'],
            description=product['description'],
            unit_price=product['unit_price'],
            user=user,
            quantity=product['quantity']
        )
        print(f"Successfully stored {new_product.name} owned by {user.name}.")


def update_stock(product_id, new_quantity):
    """Update the stock quantity of a product."""
    try:
        product = models.Product.get_by_id(product_id)
    except models.Product.DoesNotExist:
        print('Unfortunately, the requested product does not exist.')
    else:
        product.quantity = new_quantity
        product.save()
        print(f'Successfully updated the quantity of {product.name}.')
        print(f'New quantity: {product.quantity}.')


def purchase_product(product_id, buyer_id, quantity):
    """Handle the purchase of a given product."""
    try:
        product = models.Product.get_by_id(product_id)
        buyer = models.User.get_by_id(buyer_id)
    except models.Product.DoesNotExist:
        print('Unfortunately, the requested product does not exist.')
    except models.User.DoesNotExist:
        print('Unfortunately, the requested buyer does not exist.')
    else:
        if quantity > product.quantity:
            print('Unfortunately, the requested quantity is not available.')
            return
        else:
            models.Purchase.create(
                buyer=buyer,
                bought_product=product,
                quantity=quantity,
                transaction_date=datetime.now()
            )
            print(f'Successfully sold {product.name} to {buyer.name}.')
            new_quantity = product.quantity - quantity
            update_stock(product.id, new_quantity)


def remove_product(product_id):
    """Remove a product from a user."""
    try:
        product = models.Product.get_by_id(product_id)
    except models.Product.DoesNotExist:
        print('Unfortunately, the requested product does not exist.')
    else:
        product.delete_instance()
        print(f'Sucessfully removed {product.name}.')


if __name__ == '__main__':
    if not os.path.exists(models.DATABASE):
        create_tables()
        fill_tables()

    # search('game')
    # list_user_products(4)
    # list_products_per_tag(1)
    # add_product_to_catalog(1, {
    #     'name': 'diamond painting set',
    #     'description': 'Very beautiful set. A perfect gift for friends',
    #     'unit_price': 9.99,
    #     'quantity': 2,
    # })
    # update_stock(1, 10)
    # purchase_product(2, 6, 1)
    # remove_product(11)
