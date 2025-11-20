# This function returns a Life Stage profile based on age
def generate_profile(age: int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# Collect user name
user_name = input("Enter your full name: ")

# Collect birth year and calculate age
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Collect favorite hobbies
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

# Generate life stage
life_stage = generate_profile(current_age)

# Create user profile dictionary (digital user card)
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Display user profile summary
print(f"\n---\nProfile Summary:\nName: {user_profile['name']}\nAge: {user_profile['age']}\nLife Stage: {user_profile['stage']}")
if user_profile["hobbies"]:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f"- {hobby}")
else:
    print("You didn't mention any hobbies.")
print("---")