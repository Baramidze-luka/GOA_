#  გააკეთეთ Filter Even Numbers. მიზანი: გაფილტრეთ ყველრა ლუწი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ

my_list = []


i = 0

for i in range(20):
    if i % 2 == 0:
        my_list.append(i)
        print(my_list)