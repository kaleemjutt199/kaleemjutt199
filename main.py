import os
import platform

# Clear screen function
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Mean calculator
def mean(values):
    return sum(values) / len(values)

# Correlation calculator
def calculate_correlation(X, Y):
    n = len(X)
    mean_X = mean(X)
    mean_Y = mean(Y)

    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    denominator_x = sum((X[i] - mean_X) ** 2 for i in range(n))
    denominator_y = sum((Y[i] - mean_Y) ** 2 for i in range(n))

    denominator = (denominator_x * denominator_y) ** 0.5

    if denominator == 0:
        return 0

    r = numerator / denominator
    return r

# Regression line calculator
def calculate_regression_line(X, Y):
    n = len(X)
    mean_X = mean(X)
    mean_Y = mean(Y)

    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(n))
    b = numerator / denominator
    a = mean_Y - b * mean_X

    return a, b

# Correlation interpretation
def interpret_correlation(r):
    print(f"\nCorrelation Coefficient (r): {r:.3f}")
    if r == 1:
        print("Perfect positive correlation ✅")
    elif r > 0.7:
        print("Strong positive correlation 📈")
    elif r > 0.3:
        print("Moderate positive correlation")
    elif r > 0:
        print("Weak positive correlation")
    elif r == 0:
        print("No correlation ❌")
    elif r > -0.3:
        print("Weak negative correlation")
    elif r > -0.7:
        print("Moderate negative correlation")
    elif r > -1:
        print("Strong negative correlation 📉")
    elif r == -1:
        print("Perfect negative correlation ✅")

# Prediction mode
def predict_values(a, b):
    while True:
        choice = input("\nDo you want to enter an X or Y value? (x/y or q to quit): ").lower()
        if choice == 'x':
            try:
                x_val = float(input("Enter X value: "))
                y_val = a + b * x_val
                print(f"Predicted Y = {a:.2f} + {b:.2f} * {x_val:.2f} = {y_val:.2f}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 'y':
            if b == 0:
                print("Cannot compute X when slope is 0.")
            else:
                try:
                    y_val = float(input("Enter Y value: "))
                    x_val = (y_val - a) / b
                    print(f"Predicted X = ({y_val:.2f} - {a:.2f}) / {b:.2f} = {x_val:.2f}")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == 'q':
            print("Exiting prediction mode.")
            break
        else:
            print("Please enter 'x', 'y', or 'q'.")

# === Main Program ===
clear_screen()
print("=== Correlation and Regression Calculator ===")

try:
    n = int(input("Enter number of data points: "))

    X = []
    Y = []

    for i in range(n):
        x = float(input(f"Enter X[{i + 1}]: "))
        y = float(input(f"Enter Y[{i + 1}]: "))
        X.append(x)
        Y.append(y)

    r = calculate_correlation(X, Y)
    interpret_correlation(r)

    a, b = calculate_regression_line(X, Y)
    print(f"\nRegression Equation: Y = {a:.2f} + {b:.2f}X")

    predict_values(a, b)

except ValueError:
    print("Invalid input. Please enter only numbers.")
