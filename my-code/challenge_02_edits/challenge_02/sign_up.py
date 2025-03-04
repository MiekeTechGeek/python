from roles import roles_list

class SignUp:
    def __init__(self):
        self.first_name = input("What is your first name: ").strip().title()
        self.second_name = input("What is your last name: ").strip().title()
        self.email = input("What is your email: ").strip()

        # Create a dictionary mapping role names to Role objects
        roles = {role.name: role for role in roles_list}

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


if __name__ == "__main__":
    signup = SignUp()
    print(f"User signed up as {signup.position}")