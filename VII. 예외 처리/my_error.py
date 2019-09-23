#p219
class OddError(Exception):
    def __init__(self):
        self.message = message

    def __str__(self):
        return self.message

n=11
try:
    if n % 2 != 0:
        raise OddError
    else:
        print("짝수에요. 짝짝짝")

except OddError as e :
    print(e)