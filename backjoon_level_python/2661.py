def solve(n: int) -> str:
    success: bool = False
    answer: str = ''

    def dfs(progression: str):
        nonlocal success, answer

        if success:
            return
        if len(progression) == n:
            success = True
            answer = progression
            return
        for number in numbers:
            if promising(progression + number):
                dfs(progression + number)
    dfs('')
    return answer


def promising(text: str) -> bool:
    """
    12345678 입력받으면
    7 == 8
    56 == 78
    345 == 678
    1234 == 5678
    비교함
    """
    text_length = len(text)

    for i in range(1, text_length//2+1):
        if text[text_length-i:text_length] == text[text_length-i-i:text_length-i]:
            return False
    return True


if __name__ == '__main__':
    N = int(input())
    numbers = ['1', '2', '3']
    print(solve(N))