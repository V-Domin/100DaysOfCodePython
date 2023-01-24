# from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
from prettytable import from_csv

my_skills_table = PrettyTable()

skills = [
    ["English", "Advanced", "6 years", "Work/Study"],
    ["German", "Intermediate", "1 year", "Hobby"],
    ["Python", "Intermediate", "less then 1 year", "Future job"],
    ["Django", "Intermediate", "6 months", "Future job"],
    ["Self-Development", "Upper-Intermediate", "3 years", "Myself"],
]


my_skills_table.field_names = ["Name", "Level", "How long", "Area of Usage"]
my_skills_table.add_rows(skills)
my_skills_table.align = "l"

print(my_skills_table)

