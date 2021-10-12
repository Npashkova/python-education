"""Module that demonstrates communication in the restaurant via OOP classes."""
from abc import ABC
from abc import abstractmethod


class Restaurant:
    """Attributes: name and phone_number
    Methods: take_orders, get_cooked_orders, give_cooked_orders
    """
    name = 'Cozy place'
    phone_number = '096-222-0788'

    @classmethod
    def greet_customers(cls):
        """Just say hello"""
        print(f'We welcome you in our restaurant "{cls.name}"!')

    @staticmethod
    def give_cooked_orders(customer_type, customer_id):
        """Give cooked orders to waiter or courier"""
        Kitchen.get_cooked_orders()
        if customer_type == 'phone customer':
            Courier.deliver_orders(customer_id)
        else:
            Waiter.give_cooked_order(customer_id)


class Menu:
    """Keeps different dishes"""
    salad = ['Greece', 'Cesar', 'Sea']
    pasta = ['Carbonara', 'Seafood', 'Meat']
    soup = ['Gazpacho', 'Mushroom', 'Cheese']
    dessert = ['Pavlova', 'Ice cream', 'Tiramisu']
    beverage = ['Beer', 'Wine', 'Tea', 'Coffee', 'Juice']
    menu_dict = {'salad': 80, 'pasta': 100, 'soup': 70, 'dessert': 50, 'beverage': 40}


class Kitchen:
    """Attributes: orders_to_cook
    Methods: get_orders, get_cooked_orders"""
    orders_to_cook = None

    @classmethod
    def get_orders(cls, orders):
        """Get orders from restaurant"""
        cls.orders_to_cook = orders
        return cls.orders_to_cook

    @staticmethod
    def get_cooked_orders():
        """Get orders from cooks"""
        cooked_orders = Cook.cooked_orders
        return cooked_orders


class Employee(ABC):
    """Abstract class for a
    waiter, an administrator, a cook and a courier
    """
    def __init__(self, name, real_salary):
        """Constructor that has 2 attributes:
        name and salary (pay with bonuses)
        """
        self.name = name
        self.real_salary = real_salary

    @abstractmethod
    def work(self):
        """Prints out the type of work"""
        print('I can work')

    @staticmethod
    def get_salary(role):
        """Keeps amount of salary at rate for roles"""
        salaries = {'waiter': 15000, 'administrator': 12000, 'cook': 18000, 'courier': 10000}
        return f'My salary at rate:{salaries.get(role)}'


class Cook(Employee):
    """Has method: cook_orders, which means popping orders
    from the list and attribute cooked_orders
    """
    cooked_orders = []

    def work(self):
        """Prints out the type of work"""
        print('I can cook dishes')

    @classmethod
    def cook_orders(cls, orders_list):
        """Pops the object that has been cooked"""
        popped_object = orders_list.pop()
        cls.cooked_orders.append(popped_object)
        return cls.cooked_orders


# cook_1 = Cook('Vlad', 20000)
# print(cook_1.get_salary('cook'))
# print(cook_1.real_salary)
class Administrator(Employee):
    """Has methods accept_phone_orders and control_quality"""
    def work(self):
        """Prints out the type of work"""
        print('I can accept phone orders and control quality')

    @staticmethod
    def accept_phone_orders(waiter, customer_type, customer_id):
        """Create order for a phone customer
        """
        if customer_type == 'phone customer':
            order = Order(order_id=customer_id, list_of_dishes=[], customer_id=customer_id)
            waiter.orders_list.append(order)
        else:
            print('Please, wait for your waiter')

    @staticmethod
    def control_quality():
        """Just say everything is OK and be polite"""
        print('Hello! I hope that you like everything. Have a good day!')


class Waiter(Employee):
    """Create and work with orders, make customer happy"""
    def __init__(self, name, real_salary, orders_list):
        super().__init__(name, real_salary)
        self.orders_list = orders_list
        self.amount = 0

    def work(self):
        """Prints out the type of work"""
        print('I can create and work with orders, make customer happy')

    def create_order(self, customer_id):
        """Creates order object"""
        order = Order(order_id=customer_id, list_of_dishes=[], customer_id=customer_id)
        self.orders_list.append(order)

    def extend_order(self, customer_id, list_of_dishes):
        """Add dishes to order object"""
        for obj in self.orders_list:
            if obj.customer_id == customer_id:
                obj.list_of_dishes.append(list_of_dishes)

    @staticmethod
    def give_cooked_order(customer_id):
        """Give orders to customer"""
        for order in Cook.cooked_orders:
            if order.order_id == customer_id:
                return order.list_of_dishes
        return None

    def collect_money(self, list_of_dishes):
        """Count sum of the order"""
        for key, value in Menu.menu_dict.items():
            for dish in list_of_dishes:
                if key == dish:
                    self.amount += value
        return self.amount

    def clean_orders_list(self):
        """Clean orders_list"""
        self.orders_list.clear()


class Courier(Employee):
    """Has transport and can deliver orders"""
    def __init__(self, name, real_salary, transport):
        super().__init__(name, real_salary)
        self.transport = transport

    def work(self):
        """Prints out the type of work"""
        print('I can deliver orders to customer')

    @staticmethod
    def deliver_orders(customer_id):
        """Give list_of_dishes to a phone customer"""
        for order in Cook.cooked_orders:
            if order.order_id == customer_id:
                return order.list_of_dishes
        return None


class Order:
    """Keeps information about order"""
    def __init__(self, order_id, list_of_dishes, customer_id):
        """Constructor"""
        self.order_id = order_id
        self.list_of_dishes = list_of_dishes
        self.customer_id = customer_id


class Customer:
    """Attributes: customer_id, customer_type
    Methods: make_order, receive_dishes, give_money"""
    def __init__(self, customer_id, customer_type):
        """Constructor"""
        self.customer_id = customer_id
        self.customer_type = customer_type

    @staticmethod
    def make_order(*items):
        """Generates a list of dishes"""
        list_of_dishes = [*items]
        return list_of_dishes

    def receive_dishes(self):
        """Just receive list of dishes"""
        Waiter.give_cooked_order(self.customer_id)
        return 'Thank you'

    @staticmethod
    def give_money(waiter):
        """Returns some float"""
        sum_to_pay = waiter.amount + waiter.amount * 0.1
        return sum_to_pay


Restaurant.greet_customers()
customer_1 = Customer('1', 'phone customer')
customer_2 = Customer('2', 'call customer')
list_of_dishes_1 = customer_1.make_order('salad', 'beverage')
list_of_dishes_2 = customer_2.make_order('soup', 'pasta')
waiter_1 = Waiter('Dima', '17000', [])
waiter_2 = Waiter('Vova', '16000', [])
admin = Administrator('Clara', '15000')
admin.accept_phone_orders(waiter_1, customer_1.customer_type, customer_1.customer_id)
waiter_1.extend_order(customer_1.customer_id, list_of_dishes_1)
waiter_2.create_order(customer_2.customer_id)
waiter_2.extend_order(customer_2.customer_id, list_of_dishes_2)
# for order in waiter_2.orders_list:
#     print(order.list_of_dishes)
#     print(order.customer_id)
Kitchen.get_orders(waiter_2.orders_list)
cook_1 = Cook('Ivan', 20000)
cook_1.cook_orders(Kitchen.orders_to_cook)
Kitchen.get_cooked_orders()
Restaurant.give_cooked_orders(customer_1.customer_id, customer_1.customer_type)
waiter_2.give_cooked_order(customer_1.customer_id)
customer_1.receive_dishes()
waiter_2.collect_money(list_of_dishes_2)
print(customer_1.give_money(waiter_2))
Kitchen.get_orders(waiter_1.orders_list)
cook_1 = Cook('Ivan', 20000)
cook_1.cook_orders(Kitchen.orders_to_cook)
Kitchen.get_cooked_orders()
courier = Courier('Kirill', 12000, 'bicycle')
Restaurant.give_cooked_orders(customer_2.customer_id, customer_2.customer_type)
courier.deliver_orders(customer_2.customer_id)
customer_2.receive_dishes()
waiter_1.collect_money(list_of_dishes_1)
print(customer_2.give_money(waiter_1))