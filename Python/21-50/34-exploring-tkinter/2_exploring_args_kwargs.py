# def add(*args):
#     sum = 0

#     for num in args:
#         sum += num

#     return sum

# print(add(2, 3, 4))


# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")  # self.make = kw["make"]
#         self.model = kw.get("model")  # self.model = kw["model"]


# my_car = Car(make="Nissan")
# print(my_car.make)
# print(my_car.model)
