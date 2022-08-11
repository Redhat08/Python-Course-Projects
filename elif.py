annualSales = 500000
region = "West"
newCustomer = True


if annualSales >= 500000:
    print("Dear Platinum Customer")

elif annualSales >= 300000:
    print("Dear Gold Customer")

elif not annualSales <= 100000 and newCustomer:
    print("Dear Silver Customer")

    if region == "South":
        print("")


else:
    print("Dear Up and Coming Customer, ")


    def fullName(firstName, lastName):
        print(f"{firstName}, {lastName}")

fullName("Indigo", "Devine")

print("thank you for purchasing")
print("We are highly appreciative!")
