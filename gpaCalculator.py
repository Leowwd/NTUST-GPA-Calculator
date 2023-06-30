dic1 = {"A+":4.3, "A":4.0, "A-":3.7, "B+":3.3, "B":3.0, "B-":2.7, "C+":2.3, "C":2.0, "C-":1.7, "D":1.0, "E":0.0, "X":0.0}
dic2 = {}
dic3 = {}
dic4 = {"GE":0, "FE":0, "廢物國文":0}

with open("gpa.csv", "r") as putin: #直接把成績查詢那邊複製下來 放到gpa.csv

    while True:
        ques = input("Do you want to study abroad? (please enter Y or N or R and enter E to exit)\n").lower()
        if ques == "y":
            dic1["A+"] = 4
        elif ques == "n":
            dic1["A+"] = 4.3
        elif ques == "e":
            break

        for i in putin.readlines():
            temp = i.split(",")

            if temp[2].startswith("CC") and temp[3].startswith("英") and temp[6] != "免修" or temp[2].startswith("FE"):
                dic4["FE"] += int(temp[4])

            if temp[6] != "二次退選" and temp[6] != "抵免" and temp[6] != "免修" and temp[5] != "成績未到":
                if temp[7] != "":
                    dic4["GE"] += int(temp[4])
                if temp[2].startswith("CC") and len(temp[2]) == 9:
                    dic4["廢物國文"] += int(temp[4])
                if temp[5] not in dic2 and temp[5] not in dic3:
                    dic2.setdefault(temp[5], 1)
                    dic3.setdefault(temp[5], int(temp[4]))
                else:
                    dic2[temp[5]] += 1
                    dic3[temp[5]] += int(temp[4])
        total = 0
        totalCredit = 0
        for grade, credit in dic3.items():
            total += dic1[grade] * credit
            totalCredit += credit

        if ques == "y" or ques == "n":
            print("-" * 50)
            print(f"Your gpa is {round(total/totalCredit, 2)}")
            print("-" * 50)

        if ques == "r":
            print("-" * 50)
            print(dic2) #總共幾堂課是啥分數
            print("-" * 50)
            print(dic3) #總共幾學分是啥分數
            print("-" * 50)            
            print(dic4)

            print("-" * 50)            
            if dic4["GE"] >= 15:
                print("You've passed threshold of GE.")
            else:
                g = 15 - dic4["GE"]
                print(f"GE: You need {g} credits.") if g > 1 else print(f"GE: You need {g} credit.")
            print("-" * 50)

            if dic4["FE"] >= 12:
                print("You've passed threshold of English.")
            else:
                g = 12 - dic4["FE"]
                print(f"English: You need {g} credits.") if g > 1 else print(f"English: You need {g} credit.")
            print("-" * 50)

            if dic4["廢物國文"] >= 6:
                print("You've passed threshold of 廢物國文.")
            else:
                g = 6 - dic4["廢物國文"]
                print(f"廢物國文: You need {g} credits.") if g > 1 else print(f"廢物國文: You need {g} credit.")
            print("-" * 50)