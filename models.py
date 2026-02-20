class User:
    def __init__(self, age, gender, total_income, utilities,
                 entertainment, school_fees, shopping, healthcare):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.utilities = utilities
        self.entertainment = entertainment
        self.school_fees = school_fees
        self.shopping = shopping
        self.healthcare = healthcare

    def to_list(self):
        return [
            self.age,
            self.gender,
            self.total_income,
            self.utilities,
            self.entertainment,
            self.school_fees,
            self.shopping,
            self.healthcare
        ]
