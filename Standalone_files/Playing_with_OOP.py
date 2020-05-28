class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = str(color)
        self.waist_size = int(waist_size)
        self.length = int(length)
        self.price = float(price)
    def change_price(self, new_price):
        self.price = float(new_price)
    def discount(self, discount):
        return self.price * (1-discount)

def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()

class SalesPerson:

    def __init__(self, first_name, last_name, employee_id, salary, pants_sold = [], total_sales = 0):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.employee_id = int(employee_id)
        self.salary = float(salary)
        self.pants_sold = pants_sold
        self.total_sales = total_sales

    def sell_pants(self, pants_sold):
        self.pants_sold.append(pants_sold)

    def display_sales(self):
        for i in self.pants_sold:
            print("color: " + i.color + ", waist_size: " + str(i.waist_size) + ", length: " + str(i.length) + \
                  ", price: " + str(i.price))

    def calculate_sales(self):
        total_sales = 0
        for i in self.pants_sold:
            total_sales += i.price
        return total_sales

    def calculate_commission(self, percentage):
        return percentage * self.calculate_sales()
def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()
    