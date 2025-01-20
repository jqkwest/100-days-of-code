def life_in_weeks(age: int) -> int:
    weeks_to_go = (90*52)-(age*52)
    return weeks_to_go

def main():
    age = int(input("How many years old are you?"))
    
    print(life_in_weeks(age))
    
if __name__== '__main__':
    main()