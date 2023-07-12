# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.color("YellowGreen")
# timmy.shape("turtle")
# timmy.forward(100)
#
# # print(timmy)
# # print(my_screen.canvheight)
# my_screen.exitonclick()

#
# from prettytable import PrettyTable
# from prettytable.colortable import ColorTable, Themes, Theme
# my_theme = Theme()
# my_theme.default_color = Theme.format_code("\x1b[38;5;62m")
# my_theme.vertical_color = Theme.format_code("\x1b[38;5;56m")
# my_theme.horizontal_color = Theme.format_code("\x1b[38;5;56m")
# my_theme.junction_color = Theme.format_code("\x1b[38;5;57m")
# table = ColorTable(theme=my_theme)
#
#
# table.field_names = ["Name", "Date of Birth", "Gender"]
# table.add_rows(
#     [
#         ["Hannah", "05/24/05", "F"],
#         ["Ammon", "10/20/06", "M"],
#         ["Deborah", "01/23/09", "F"],
#         ["Rebekah", "06/15/11", "F"],
#         ["Simon", "10/08/14", "M"],
#         ["Sarah", "09/02/22", "F"]
#     ]
# )
# table.align["Name"] = "l"
#
# print(table)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
coinMachine = MoneyMachine()

while True:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        break
    elif order == "report":
        coffeeMaker.report()
        coinMachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeeMaker.is_resource_sufficient(drink) and coinMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
