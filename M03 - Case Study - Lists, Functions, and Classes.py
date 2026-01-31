class Automobile():
    def Vehicle(self):
        vtype = input()
        year = input()
        make = input()
        model = input()
        num_doors = input()
        roof_type = input()

        return


    print("Welcome to the Automobile Information System!\n")
    Vehicle.vtype = input("What type of vehicle do you have? (e.g., car, truck, plane, boat, or broomstick) ")
    Vehicle.year = input("What is the year of your vehicle? ")
    Vehicle.make = input("What is the make of your vehicle? ")
    Vehicle.model = input("What is the model of your vehicle? ")
    Vehicle.num_doors = input("How many doors does your vehicle have? ")
    Vehicle.roof_type = input("What is the roof type of your vehicle? (solid or sunroof) ")

    print((lambda Vehicle: f"\nVehicle Information:\n\nType: {Vehicle.vtype.capitalize()}\nYear: {Vehicle.year}\nMake: {Vehicle.make.capitalize()}\nModel: {Vehicle.model.capitalize()}\nNumber of Doors: {Vehicle.num_doors}\nRoof Type: {Vehicle.roof_type.capitalize()}")(Vehicle))

    print("\nThank you for using the Automobile Information System!\nHave a great day and hope to see you again soon!\n")
