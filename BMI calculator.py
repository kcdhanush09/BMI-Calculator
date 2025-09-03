x = float(input("Enter your weight (in kg): "))
y = float(input("Enter your height(in m): "))
z = x/(y**2)

while (x<0 or x>120):
    print("Invalid input")
    x = float(input("Enter your weight (in kg): "))

while (y<0 or y>2.20):
    print("Invalid input")
    y = float(input("Enter your height(in m): "))

print(f"Your BMI is {z:.2f}")
