class Policyholder:
    def __init__(self, name, policy_number, is_active=True):
        self.name = name
        self.policy_number = policy_number
        self.is_active = is_active

    def suspend(self):
        self.is_active = False

    def reactivate(self):
        self.is_active = True

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Status: {'Active' if self.is_active else 'Suspended'}")
