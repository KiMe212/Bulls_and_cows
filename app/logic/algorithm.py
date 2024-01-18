# from schemes.user import UserInfo


def search_number(options_number: str, random_number: str):
    required_number = ''.join(random_number)
    while True:
        bull, cow = 0, 0
        for i in range(0, 4):
            if required_number[i] == options_number[i]:
                bull += 1
            elif options_number[i] in required_number:
                cow += 1
        return f"{options_number} - {bull} bull(s) and {cow} cow(s)"
