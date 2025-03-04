class Role:
    def __init__(self, name, description): #we made edits to the init method so that we could create the create role function
        self.name = name
        self.description = description

# all that the repr is it is a method that allows you to represent the instance as a string
    def __repr__(self):
        return f"Role(name='{self.name}', description='{self.description}')"

# Creating instances, we edited the instances to be in line with the new init method
janitor = Role("Janitor", "Responsible for cleaning and maintenance.")
programmer = Role("Programmer", "Writes and maintains software code.")
secretary = Role("Secretary", "Handles administrative and clerical tasks.")
front_end_developer = Role("Front-end Developer", "Builds the user interface of applications.")
full_stack_developer = Role("Full-stack Developer", "Works on both front-end and back-end development.")

# Define roles_list at the module level
roles_list = [janitor, programmer, secretary, front_end_developer, full_stack_developer]

# made a program that allows us to create new roles in the terminal
def create_role():
    name = input("Enter the role name: ")
    description = input("Enter the role description: ")
    new_role = Role(name, description)
    roles_list.append(new_role)
    return new_role

def main():
    while True:
        print("\n--- Role Management ---")
        action = input("Do you want to create a new role? (yes/no): ").strip().lower()
        
        if action in ['yes', 'y']:
            new_role = create_role()
            print(f"Created {new_role}") 
            break
        elif action in ['no', 'n']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nAll Created Roles:")
    for role in roles_list:
        print(role)

if __name__ == "__main__":
    main()  # Ensure the script only runs when executed directly