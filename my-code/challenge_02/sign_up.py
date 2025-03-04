from roles import janitor, programmer, secretary, front_end_developer, full_stack_developer

class SignUp:

    def __init__(self):
        self.first_name = input("What is your first name: ")
        self.second_name = input("What is your last name: ")
        self.email = input("What is your email: ")
        
        roles = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretary": secretary, 
            "Front_end_developer": front_end_developer,
            "Full_stack_developer": full_stack_developer
        }

        print("\nAvailable Positions:")
        for role_name in roles:
            print(f"- {role_name}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in roles:
                self.position = roles[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")