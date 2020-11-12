'''
Local Enclosing Global Scope Built-in

'''

# x = 'global X'

def test():
    global x
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)
