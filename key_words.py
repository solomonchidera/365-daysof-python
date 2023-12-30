#This function will display as many arguments as you may want,
#Using keywords arguments

def multiple_skills(*skill):
    print("Hello software engineer, please insert your skills here:")

    for skills in skill:
        print(f"{skill}")

multiple_skills("html", "css")
