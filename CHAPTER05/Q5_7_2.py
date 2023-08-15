data = [
    ["001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["004", "Male", "Suzuki", "Ichirou", 35, "Hokkaidou"],
]

member_information = {}
for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info
    print("number", "information", sep="\t")
    for key, info in member_information.items():
        print(key, info)
