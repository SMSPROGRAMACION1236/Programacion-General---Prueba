
## decorators
""" It's a  special function that decorate another one, example, add another action to another function"""
# Adding code

def decorator(function): # if so the decorator function create a function that execute his code  and then execute the function in the () then another code, and the last return the new function
  def change_function():
    print("Before calling the function")
    function()
    print("After calling the asD FNH65HMNJ BCe5tsAQS  W132function")
  return change_function

# def greeting():
#   print("Hello Santiago")

# change_greeting =  decorator(greeting)
# change_greeting()


      # This is the best form to use decorator
@decorator
def greeting():
  print("Hello World!")

greeting()