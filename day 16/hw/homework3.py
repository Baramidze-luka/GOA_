#  გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული აღნაგობის ხალხს შეუძლიათ. გიორგი ზოოპარკში უშვებს ხალხს რომელიც 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს შორის არიან წონით. თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და გაარკვიოთ შეუძლია თუ არა მომხმარებელს ზოოპარკის მონახულება.

height = int(input("Enter Your Height:"))



if height >= 180:
    print("სიმაღლე დაშვებულია")
elif height < 180:
    print("სიმაღლე დაუშვებელია")

weight = int(input("Enter Your Weight:"))


if 50 < weight < 90:
    print("წონა დაშვებულია")
else:
    print("წონა დაუშვებელია")