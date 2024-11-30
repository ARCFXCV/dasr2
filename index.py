import math

# Funksiyani hisoblash uchun parametrlar
x_values = [1 + 0.1 * i for i in range(11)]  # 1 dan 2 gacha bo'lgan oraliq (1, 1.1, ..., 2)
n = 20  # n = 20
epsilon = 10**-5  # yaqinlashtirish uchun epsilon

# Funksiya
def calc_function(x, n, epsilon):
    result = 0
    term = 1
    i = 0
    
    # epsilon qiymatidan kichik bo'lmaguncha yig'ish
    while abs(term) > epsilon and i < n:
        term = ((-1)**i) * (math.factorial(2) * (x**2) + math.factorial(2*i))
        result += term
        i += 1
    
    return result

# Natijalarni chop etish
for x in x_values:
    print(f"x = {x:.1f}, f(x) = {calc_function(x, n, epsilon)}")
