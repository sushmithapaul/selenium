print("Welcome to Jenkins page")
def mygen():
    n = 1
    yield n
    n+=2
    yield n
    n+=3
    yield n
    yield "End"
for n in mygen():
    print(n)
    # print('succesful login')
    # print('What is your name?')
    # myName = input()
    # print('it is good to meet you,' + myName)
    # print('The length of your name is:')
    # print(len(myName))
    # print('what is your age?')
    # myAge = input()
    # print('you will be ' + str(int(myAge) + 1) + 'in a year')
    # print('happy seeing you')
    # password = 'markismark'
    # if password == 'ma ark':
    #     print('acess')
    # else:
    #     print('wrong password')
    #
    #
    # def hello():
    #     print('Hiii')
    #     print('Welcome to the Page')
    #     print('Thankyou !!')


    # hello()