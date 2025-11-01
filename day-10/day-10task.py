def full_name(first_name,last_name):
    """This is a docstring which defines our function and everything inside it what is does"""
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"     #return is the end of a function no other data is considered after return in function

print(full_name("Pranav","sikhWAL"))

def function1(task):
    return task+task
def function2(task):
    return task.title()
print(function1("best"))
print(function2(function1("best")))