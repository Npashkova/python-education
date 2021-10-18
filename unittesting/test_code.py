"""Unit tests for testing_code.py file"""
from testing_code import even_odd, sum_all, time_of_day, Product, Shop
import pytest
from freezegun import freeze_time

# Test for even_odd function


@pytest.mark.parametrize("item, expected", [(4, "even"), (7, "odd"), (9, "even"), (16, "odd")])
def test_even_odd(item, expected):
    """Tests if even_odd function returns correct answer"""
    assert even_odd(item) == expected


def test_not_number_even_odd():
    """Tests if even_odd function raises exception
    if string used as a parameter
    """
    with pytest.raises(TypeError):
        even_odd('15')

# Test for sum_all function


def test_sum_all():
    """Tests if function sum_all add numbers right"""
    assert sum_all(349, 99.3, -0.67) == 349 + 99.3 - 0.67


def test_incorrect_sum_all():
    """Fails because of incorrect expected number"""
    assert sum_all(349, 990) == 1099


def test_not_number_sum_all():
    """Tests if sum_all function raises exception
        if string used as a parameter
        """
    with pytest.raises(TypeError):
        even_odd('hello')

# Test for time_of_day function


def test_time_of_day():
    """Tests if time_of_day func works correct"""
    assert time_of_day() == "night"


def test_incorrect_time_of_day():
    """Fails because of incorrect expected time"""
    assert time_of_day() == "morning"


@freeze_time("11:15")
def test_time_of_day_morning():
    """Tests if time_of_day func works correct in morning
    uses freeze_time
    """
    assert time_of_day() == "morning"


@freeze_time("14:00")
def test_time_of_day_afternoon():
    """Tests if time_of_day func works correct in afternoon
       uses freeze_time
       """
    assert time_of_day() == "afternoon"

# Test for class Product


@pytest.fixture
def default_product_quantity():
    """Creates product instance with default quantity"""
    return Product('biscuits', 30)


@pytest.fixture
def new_product():
    """Creates product instance, reset quantity"""
    return Product('apple_juice', 20, 100)


def test_default_quantity(default_product_quantity):
    """Tests if default_quantity works correct"""
    assert default_product_quantity.quantity == 1


def test_setting_quantity(new_product):
    """Tests if reset quantity works correct"""
    assert new_product.quantity == 100


def test_subtract_quantity(new_product):
    """Tests method subtract_quantity"""
    new_product.subtract_quantity(10)
    assert new_product.quantity == 100 - 10


def test_add_quantity(new_product):
    """Tests method add_quantity"""
    new_product.add_quantity(45)
    assert new_product.quantity == 100 + 45


def test_change_price(new_product):
    """Tests method change_price"""
    new_product.change_price(25)
    assert new_product.price == 25


def test_price_negative_number(new_product):
    """Tests if change_price method
    raises ValueError in case of negative number
    """
    with pytest.raises(ValueError):
        new_product.change_price(-20)

# Tests for class Shop


@pytest.fixture
def empty_shop():
    """Creates empty shop instance"""
    return Shop()


@pytest.fixture
def new_shop():
    """Creates shop instance with a product"""
    mango = Product("fruit", 40, 10)
    return Shop(mango)


def test_without_products(empty_shop):
    """Tests init with no products"""
    assert empty_shop.products == []


def test_shop_with_product(new_shop):
    """Tests init with some product, must be an instance
    of Product"""
    assert isinstance(new_shop.products[0], Product)


def test_add_products(new_shop):
    """Test add_products_method
    Length should be 2
    """
    chips = Product("snack", 39, 90)
    new_shop.add_product(chips)
    assert len(new_shop.products) == 2


@pytest.mark.parametrize("item, index", [("fruit", 0), ("vegetable", None)])
def test_get_product_index_(item, index, new_shop):
    """Tests get_product_method
    with different inputs
    """
    assert new_shop._get_product_index(item) == index


def test_sell_product_bigger_value(new_shop):
    """Tests if ValueError is raised
    when sell more than quantity"""
    with pytest.raises(ValueError):
        new_shop.sell_product("fruit", 20)


@pytest.mark.parametrize("quantity, expected", [(3, 120), (5, 200)])
def test_sell_product_receipt_counter(new_shop, quantity, expected):
    """Tests if receipt is counted correct"""
    assert new_shop.sell_product("fruit", quantity) == expected


def test_money_after_selling(new_shop):
    """Tests if money is added after selling"""
    new_shop.sell_product("fruit", 4)
    assert new_shop.money == 4 * 40


def test_sell_product_del(new_shop):
    """Tests if sell_product method delete
    product when sold quantity == quantity
    """
    new_shop.sell_product("fruit", 10)
    assert len(new_shop.products) == 0


def test_sell_product_subtract(new_shop):
    """Tests if subtract method works
    when sell products
    """
    new_shop.sell_product("fruit", 7)
    assert new_shop.products[0].quantity == 3
