
class USD:
    def get_value(self):
        return 3.52

    def calculate(self, amount):
        return amount * self.get_value()


class ILS:
    def get_value(self):
        return 0.28

    def calculate(self, amount):
        return amount * self.get_value()


def get_user_value():
    while True:     # the loop is true
        try:
            choice = input("Please choose an option (1/2):")    # input 1 / 2
            if choice == '1':    # if the user choose 1
                amount = float(input("Please enter an USD amount to convert: "))  # USD amount to convert
                usd = USD()
                print('$', amount, 'USD to ILS is: ₪', usd.calculate(amount))
                text = open('C://Users/shayo/Project.txt', 'a')
                text.write('ILS ' + str(usd.calculate(amount)) + '\n')
                text.close()
            elif choice == '2':     # if the user choose 2
                amount = float(input("Please enter an ILS amount to convert: "))  # ILS amount to convert
                ils = ILS()
                print('₪', amount, 'ILS to USD is: $', ils.calculate(amount))
                text = open('C://Users/shayo/Project.txt', 'a')
                text.write('USD ' + str(ils.calculate(amount)) + '\n')
                text.close()
            else:
                print('Invalid input.')
                continue
            keep()
        except ValueError:
            print("Invalid input.")
            continue


def keep():
    while True:
        try:
            keep_calculate = input("Would you like to try again? (Y / N): ")    # if the user want to convert again
            if keep_calculate == 'y':
                get_user_value()
            elif keep_calculate == 'n':
                print("Thanks for using our currency converter")
                print("All Previous results:")
                text = open('C://Users/shayo/Project.txt', 'r')
                print(text.read())
                text.close()
                open('C://Users/shayo/Project.txt', 'w').close()  # deletes file data when user press 'n' for next print
                quit()
        except ValueError:
            print("Invalid input.")


def main():
    print("Welcome to currency converter\n1 ) \tConvert USD to ILS\n2 ) \tConvert ILS to USD")
    get_user_value()


main()