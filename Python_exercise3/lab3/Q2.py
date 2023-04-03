"""
Yinglin Lu 2212059
class encapsulation/properties/Inheritance
Nov 12, 2022
This is Q2
"""
from datetime import date


class Profile:
    """
     class Profile calculate age, max heart rate, target heart range, BMI(body mass index)
     givem name, gender, bithdate, height, weight
     """

    def __init__(self, firstName, lastName, gender, birthYear, birthMonth, birthDay, height, weight):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__birthYear = birthYear
        self.__birthMonth = birthMonth
        self.__birthDay = birthDay
        self.__height = height
        self.__weight = weight

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, value):
        self.__firstName = value

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, value):
        self.__lastName = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def birthYear(self):
        return self.__birthYear

    @birthYear.setter
    def birthYear(self, value):
        self.__birthYear = value

    @property
    def birthMonth(self):
        return self.__birthMonth

    @birthMonth.setter
    def birthMonth(self, value):
        self.__birthMonth = value

    @property
    def birthDay(self):
        return self.__birthDay

    @birthDay.setter
    def birthDay(self, value):
        self.__birthDay = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @property
    def birthdate(self):
        return str(date(self.birthYear, self.birthMonth, self.birthDay))

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthYear - ((today.month, today.day) < (self.birthMonth, self.birthDay))

    @property
    def maxHeartRate(self) -> int:
        return 220 - self.age

    @property
    def targetHeartRateRange(self) -> str:
        return f"{0.5 * self.maxHeartRate:.0f}-{0.85 * self.maxHeartRate:.0f}"

    @property
    def BMI(self) -> int:
        """
        Formula: weight (lb) / [height (in)]^2 x 703
        :return: body mass index
        """
        return round((self.weight / self.height ** 2) * 703)

    def __repr__(self):
        return (
            f"First Name: {self.firstName:<20s}Last Name: {self.lastName:<20s}Gender: {self.gender:<5s}Birthdate: {self.birthdate:<15s}Height(inches): {self.height:<10.2f}Weight(lbs): {self.weight:<5.2f}\n"
            f"Age: {self.age:<10d}Maximum Heart Rate(beats/minute): {self.maxHeartRate:<10d}Target Heart Range(beats/minute): {self.targetHeartRateRange:<10s} BMI(body mass index): {self.BMI}")


def main():
    while True:
        try:
            firstName, lastName = input(
                "Please enter your first name and last name seperated by comma(all letters(space,'-' allowed), min 1 char,max 20 chars):").strip().split(',')
            for name in (firstName, lastName):
                if not (0 < len(name) <= 20 and name.replace(" ", "").replace("-", "").isalpha()):
                    raise ValueError("Error: Invalid input! "
                                     "First Name and Last Name must be all letters(space and '-' are allowed)"
                                     " and their lengths are 1-20 characters!")
            else:
                break
        except ValueError as v:
            print(v)

    while (gender := input("Please enter your gender(M/F): ").strip().upper()) not in ('M', 'F'):
        print("Invalid input! Gender must be 'M' or 'F'!")

    while True:
        try:
            birthYear, birthMonth, birthDay = map(int, input(
                "Please enter your birthdate in following format (YYYY-MM-DD):").strip().split('-'))
            birthdate = date(birthYear, birthMonth, birthDay)
            if birthdate <= date.today():
                break
            else:
                raise ValueError("Error: Invalid input! Your birthdate cannot surpass today!")

        except ValueError as v:
            print(v)

    while True:
        try:
            height, weight = map(float, input(
                "Please enter your height(inches) and weight(lbs) seperated by comma:").strip().split(','))
            if height > 0 and weight > 0:
                break
            else:
                raise ValueError("Error: Invalid input! Height and weight must be positive!")
        except ValueError as v:
            print(v)

    person = Profile(firstName, lastName, gender, birthYear, birthMonth, birthDay, height, weight)
    print(person)


main()
