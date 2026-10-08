# def using_dic(**details):
#     for key, value  in details.items():
#         print(key, ":", value)


# using_dic(
#     username="Naman",
#     role = "ANALYST",
#     active=True
# )



# def address(**giveME):
#     for key,value in giveME.items():
#         print(key,":",value)

# address(
#     city="Ayodhya",
#     block ="Milkipur",
#     mall="sau"
# )


def test(name , *arg, **kwargs):
    print("Name:",name)
    print("Args:",arg)
    print("Kwargs:",kwargs)

test(
    "Naman",
    10,
    20,
    role="student",
    active=True
)