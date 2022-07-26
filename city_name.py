#def get_counrty (country_name, city_name):
    #"""return a country_name and city_name"""
    #country_name = f"{country_name} {city_name}"
    #return country_name.title()
#country = get_counrty("united states","new york city")
#print(country)

from turtle import *

bgcolor("black")
speed(0)
hideturtle()

for i in range (120):
    color("magenta")
    circle(i)
    color("cyan")
    circle(i * 0.8)
    right(3)
    forward(3)
done()