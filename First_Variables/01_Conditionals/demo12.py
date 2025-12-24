#match case

#age = 2

#if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
#    category = "Toddler"
#elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9:
#    category = "Kid"
#elif age == 10 or age == 11 or age == 12 or age == 13 or age == 14 or age == 15 or age == 16 or age == 17:
#    category = "Teen"
#elif age >= 18:
#    category = "Adult"
#else:
#    category = "big adult"

#print(category)
# using match case

age = 2  
match age:
    case 0 | 1 | 2 | 3 | 4:
        category = "Toddler"
    case 5 | 6 | 7 | 8 | 9:
        category = "Kid"
    case 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17:
        category = "Teen"
    case age if age >= 18:
        category = "Adult"
    case _:
        category = "big adult"      
print(category)