from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from prettytable import PrettyTable

x = PrettyTable()

x.field_names = (['ID', 'People', 'Salary'])

x.add_row([1, 'Ivanov', 100])
x.add_row([2, 'Petrov', 200])
x.add_row([3, 'Smit', 300])

date_now = datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(x)
    print(date_now)
