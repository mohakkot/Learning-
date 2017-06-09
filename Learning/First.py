def allowed_limit(my_age):
    girls_age=my_age/2 + 7
    return girls_age

for x in range(15,60):
    age_allowed = allowed_limit(x)
    print('for boys of age:  ',x, r" allowed girl's age is:  ",  age_allowed )