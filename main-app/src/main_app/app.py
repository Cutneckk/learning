from abc import ABC, abstractmethod
from typing import List, Tuple, Dict
from main_app.tools import EmailValidator, QuantityValidator

class User:
    """класс пользователя"""

    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    def get_data(self) -> Dict[str, str]:
        return {'name': self._name, 'email': str(self._email)}


class Product:
    """Товар"""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_data(self) -> Dict[str, float]:
        return {'name': self._name, 'price': self._price}


class Calculator(ABC):
    @abstractmethod
    def get_total_price(self, cart: List[Tuple[str, float, int]]) -> float:
        pass


class PriceCalculator(Calculator):
    """калькулятор рассчета стоимости заказа"""

    def get_total_price(self, cart: List[Tuple[str, float, int]]) -> float:
        return sum(
            product_price * quantity
            for _, product_price, quantity
            in cart
        )


class ShoppingCart:
    def __init__(self):
        self.items: List[Tuple[Product, int]] = []  # protected инкапсуляция

    def get_data(self) -> List[Tuple[Product, int]]:
        return self.items


class CartReader:
    """информация содержимого корзины"""

    @staticmethod
    def get_cart_items(items: List[Tuple[Product, int]]) -> List[Tuple[str, float, int]]:
        result = []
        for product, quantity in items:
            info = product.get_data()
            result.append((info['name'], info['price'], quantity))
        return result


class CartModifier:
    def __init__(self, cart: ShoppingCart, qt_validator: QuantityValidator):
        self._cart = cart
        self._qt_validator = qt_validator # агрегация

    def set_product(self, product: Product, quantity: int) -> str:
        validated_quantity = self._qt_validator.validate(quantity)
        self._cart.items.append((product, validated_quantity))
        return 'Product added'


class CartPricing:
    """рассчет стоимости корзины"""

    def __init__(self, cart: ShoppingCart, calculator: Calculator):
        self._cart = cart
        self._reader = CartReader()  # композиция
        self.__calculator = calculator  # private инкапсуляция + агрегация

    def get_total_price(self) -> float:
        items = self._cart.get_data()
        return self.__calculator.get_total_price(self._reader.get_cart_items(items))


class Order:
    """заказ"""

    def __init__(self, user: User, cart: ShoppingCart, price: CartPricing):
        self.user = user  # агрегация
        self.cart = cart
        self.price = price
        self.items = CartReader()


class OrderInfo:
    """получение информации заказа"""

    def __init__(self, order: Order):
        self._order = order  # агрегация

    def get_order_info(self) -> Dict:
        customer = self._order.user.get_data()
        items = self._order.items.get_cart_items(self._order.cart.get_data())
        total_price = self._order.price.get_total_price()
        return {
            'Customer': customer['name'],
            'Items': items,
            'Total Price': total_price
        }


if __name__ == '__main__':
    email_validator = EmailValidator()
    quantity_validator = QuantityValidator()

    email = email_validator.validate('qwe@mail.ru')
    user = User('Max', email)
    product = Product('PC', 1000)
    product2 = Product('PC2', 2000)

    cart = ShoppingCart()
    cart_modifier = CartModifier(cart, quantity_validator)
    cart_modifier.set_product(product, 2)
    cart_modifier.set_product(product2, 1)

    calculator = PriceCalculator()
    cart_pricing = CartPricing(cart, calculator)

    order = Order(user, cart, cart_pricing)
    order_info = OrderInfo(order)
    print(order_info.get_order_info())