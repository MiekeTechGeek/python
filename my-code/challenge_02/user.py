# MAIN CHALLENGES:
# Create 2 more job positions to select from.
# Make a method that prints out the user instances' details.

# TIPS:
# Extra points if you show team synergy (get as many members to demo different sections)

from sign_up import SignUp

class User:

    def __init__(self):
        signup = SignUp()  
        self.user_first_name = signup.first_name
        self.user_second_name = signup.second_name
        self.user_email = signup.email
        self.user_position = signup.position 