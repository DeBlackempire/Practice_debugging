def divided_by(operand):
    try:
        return 50/operand
    except ZeroDivisionError:
        return 'Zero cannot divide the number'
    else:
        # noinspection PyUnreachableCode
        return 'No'
    finally:
        pass

# put = input()

print(divided_by(8))
print(divided_by(6))
print(divided_by(0))
print(divided_by(2))
print(divided_by(1))

user = input('Enter number: ')
try:
    user_input = int(user)
    x = 30/user_input
except ZeroDivisionError:
    print('zero cannot divide any number')
except ValueError:
    print('Not a number')
else:
    print(x)
finally:
    print('thanks')

# import traceback
# try:
#     raise Exception('This is the error message')
# except:
#     errorFile = open('errorinfo.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()

