import pytest
from main_app.app import User, Product, ShoppingCart, CartModifier, PriceCalculator, CartPricing, Order, OrderInfo
from main_app.tools import EmailValidator, QuantityValidator


@pytest.fixture
def setup_order():
    email_validator = EmailValidator()
    quantity_validator = QuantityValidator()

    email = email_validator.validate('qwe@mail.ru')
    user = User('Max', email)
    product = Product('PC', 1000)
    product_2 = Product('PC2', 2000)

    cart = ShoppingCart()
    cart_modifier = CartModifier(cart, quantity_validator)
    cart_modifier.set_product(product, 2)
    cart_modifier.set_product(product_2, 1)

    calculator = PriceCalculator()
    cart_pricing = CartPricing(cart, calculator)

    return Order(user, cart, cart_pricing)

class TestUser:
    def test_user_creation(self):
        user = User('Max', 'qwe@mail.ru')
        data = user.get_data()

        assert data['name'] == 'Max'
        assert data['email'] == 'qwe@mail.ru'

class TestProduct:
    def test_product_data(self):
        product = Product('PC', 1000)
        data = product.get_data()

        assert data['name'] == 'PC'
        assert data['price'] == 1000

class TestOrder:
    def test_order_total_price(self, setup_order):
        """проверка стоимости заказа"""
        assert setup_order.price.get_total_price() == 4000

    def test_order_info(self, setup_order):
        """проверка информации заказа"""
        order_info = OrderInfo(setup_order)
        info = order_info.get_order_info()

        assert info['Customer'] == 'Max'
        assert len(info['Items']) == 2
        assert info['Total Price'] == 4000