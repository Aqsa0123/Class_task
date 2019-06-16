while True:
    a=int(input('enter no'))
    def identify(a):
        result=a%2
        if result==0:
            return (a,'its even')
        else:
            return (a,' is odd')
    print(identify(a))
