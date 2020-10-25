# import re
# string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
# print(string)
# new = re.sub('[A-Z]', '', string)
# print()
# print(new)


import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    global  run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation(if 'result=0' go back):")
    else:
        equation = input(str(previous))

    if(equation == 'quit'):
        print('Aborted.')
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()