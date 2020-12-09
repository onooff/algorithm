def solution(phone_book):
    answer = True

    phone_book.sort(key=lambda x: len(x))
    print(phone_book)

    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            print(phone_book[j][:l])
            if phone_book[i] == phone_book[j][:l]:
                return False

    return answer
