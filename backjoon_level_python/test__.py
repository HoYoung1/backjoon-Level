def validate(card_number):
    result = True

    if len(card_number) == 16:
        for s in card_number:
            if not '0'<=s<='9':
                result = False
    elif len(card_number) == 19:
        for idx, s in enumerate(card_number):
            if idx in [4, 9, 14]:
                if s != '-':
                    result = False
            else:
                if not '0' <= s <= '9':
                    result = False
    else:
        result = False
    return result


def solution(card_numbers):
    answer = []

    for card_number in card_numbers:
        # print(card_number)
        if not validate(card_number):
            answer.append(0)
            # print('not validate')
            continue
        card_number = card_number.replace("-","")
        card_number = card_number[::-1]

        odd = 0
        even = 0
        for idx, num in enumerate(card_number):
            if idx % 2 != 0:
                temp = int(num) * 2
                if temp >= 10:
                    even += (temp // 10 + temp % 10)
                else:
                    even += temp
            else:
                odd += int(num)
        # print(odd)
        # print(even)
        validation = 1 if (odd + even) % 10 == 0 else 0
        # print(validation)
        answer.append(validation)

    return answer


if __name__ == '__main__':
    assert solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]) == [1,1,0,0,0,0]

