#!/usr/bin/python
from datetime import date

#*******************************************************************************
class person:
    """
    Returns a ```Person``` object with the given name, DOB, and phone number.

    """
    import datetime
    def __init__(self, name, DOB, phone_num):
            self.name = name
            self.DOB = date(DOB[0], DOB[1], DOB[2])
            self.phone_num = phone_num
            print("A student object is now created.")

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("DOB:", self.DOB.year, self.DOB.month, self.DOB.day)
        print("phone number:", self.phone_num)
#*******************************************************************************

def main():

    '''This is how you create a new Person object and print the details.
    The constructor must include 3 arguments as listed below.'''
    aPerson = person('John Doe', (1982, 12, 15), 1)
    aPerson.print_details()

    ''' TODO: Obtain the information of 5 new people and store them in a list
        when complete print their details one at a time.'''





if __name__ == "__main__":
    main()
