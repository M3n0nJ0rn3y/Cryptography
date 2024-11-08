a = 47
mod = 5

equation = (a//mod) * mod + a%mod

if equation == a:
    print(f'{a} = {(a//mod)} * {mod} + {a%mod}')

else:
    print("Calculation incorrect.")