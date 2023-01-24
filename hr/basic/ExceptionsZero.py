rng = int(input())
for i in range(rng):
    date_input = input()
    n, d = date_input.split(" ")
    try:
        ans = int(n) / int(d)
        print(int(ans))
    except ZeroDivisionError as e1:
        print("Error Code:", "integer division or modulo by zero")
    except ValueError as e2:
        print("Error Code:", e2)

