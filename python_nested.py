class BugClass:
    @staticmethod
    def no_parameter():
        print("No parameters here")

    def another_error(self):
        print("No 'self' parameter here")


def corrected_function():
    print(INVALID_VARIABLE)

def string_format_issue():
    age = "John"
    print("Hello %s" % age)

def nested_conditions(i):
    if i < 10 and i < 5:
        print("Nested conditionals")

INVALID_VARIABLE = "This is defined after being used"
bugObject = BugClass()
bugObject.no_parameter()
bugObject.another_error()

corrected_function()

string_format_issue()

nested_conditions(3)