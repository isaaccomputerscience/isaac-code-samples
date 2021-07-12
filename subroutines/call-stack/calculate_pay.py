# Isaac Computer Science
# Iterative version of binary search
# Usage licensed under the Open Government Licence v3.0


def calculate_pay(h, r):
    """Performs a basic pay calculation"""
    pay =  h * r
    return pay


def main():
    """A simple pay calculator"""
    hours = input('Enter hours worked ')
    rate = input('Enter hourly rate ')
    hours_int = float(hours)
    rate_int = float(rate)
    pay = calculate_pay(hours_int, rate_int)
    print(f"Your pay is £{pay:.2f}")


if __name__ == '__main__':
    main()
