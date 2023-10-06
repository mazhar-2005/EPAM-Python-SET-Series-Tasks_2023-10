inputStr = input("Enter a string to repeat it: ")
inputStr = inputStr+"\n"
num = int(input("Enter a num for repeatation: "))
repeatedStr = inputStr*num
print("The str "+str(inputStr.replace("\n",""))+" is repeated "+str(num)+" times: ")
print(str(repeatedStr))