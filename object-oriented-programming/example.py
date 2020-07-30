from shirt import Shirt # import Shirt class from python file

shirt_one = Shirt('red', 'M', 'long sleeve', 35)
shirt_two = Shirt('red', 'S', 'short sleeve', 30)

print(shirt_one.price)
print(shirt_two.price)

shirt_two.price_change(45)

print(shirt_one.price)
print(shirt_two.price)

# alternatively, we can chage the attribute, like price using accessing attributes
# this approach has its own drawbacks
# so, it's recommended to change the attribute value with method
# since it brings us more flexibility, when, for example, our measure units change
# we can specify the change once inide class method and use this afterwards

shirt_one.color = 'yellow'
shirt_two.size = 'L'

print(shirt_one.color)
print(shirt_two.size)
