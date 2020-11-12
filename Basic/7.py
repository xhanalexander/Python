'''
FUNCTION

'''

# def hello_function():
#    print('Masak Air!.')

# hello_function()
# hello_function()
# hello_function()
# hello_function()
# hello_function()

'''DRY (Dont Repeat Yoursleft)'''


def Student_info(*arg, **warg):
    print(arg)
    print(warg)

course = ['math', 'art']
info = {'name': 'Dutch', 'age': 29 }

Student_info(*course, **info)
