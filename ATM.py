passwd=int(input("choice your password: "))                                     #کاربر خودش پسورد انتخاب میکنه
cash=int(input("enter your cash: "))                                        #کاربر خودش مبلغ کارت رو وارد میکنه
for i in range (3):                                     #سه بار از کاربر پسوردی که انتخاب کرده رو میپرسه اگه هر سه بار غلط باشه بریک میشه اگه درست باشه ادامه میده
    p=int(input("enter the password: "))
    if p!=passwd:
        print("worng!")
    else:
        print("passed!")
        while True:                                     #از کاربر برای عملیات سوال میکنه
            print('''
            1.your cash
            2.increase
            3.derease
            4.exit
            ''')
            choice=input("choice: ")                                        #متغیر ورودی کاربر
            if choice=="1":
                print(cash)                                     #موجودی کاربر رو چاپ میکنه
            elif choice=="2":
                q=int(input("amount: "))
                cash+=q                                     #مبلغ رو به کوجودی اضافه میکنه
                print(cash)
            elif choice=="3":
                q=int(input("amount: "))
                cash=cash-q                                     #موجودی رو ا مبلغ کم میکنه
                print(cash)
            elif choice=="4":
                print("bye")                                        #برنامه رو میبنده
                break
        break

