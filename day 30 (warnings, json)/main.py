# try:
#     file = open('data.txt')
#     dictionary = {'key':'value'}
#     print(dictionary['key'])
# except FileNotFoundError:
#     file = open('data.txt', 'w')
#     file.write("Here some text")
# except KeyError as error_message:
#     print(f'There is not such thing like {error_message}. Check out: {dictionary}')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('file was closed')
#     raise KeyError("My own error. You are 404")


height = float(input("Enter your height: "))

if height > 3:
    raise ValueError("Are you sure that you're that tall???")

weight = float(input("Enter your weight: "))

bmi = weight / height **2

print(bmi)