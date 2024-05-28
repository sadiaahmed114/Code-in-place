DOG_YRS_MULTIPLIER = 7.18  

def main():
    calendar_years = int(input("Enter an age in calendar years: "))
    dog_years = calendar_years * DOG_YRS_MULTIPLIER
    print("That's", dog_years, "in dog years!")