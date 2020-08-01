if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        book_ranges = [list(map(int, input().split())) for _ in range(M)]
        visited = [False] * (N+1)
        # print(book_ranges)

        book_ranges.sort(key=lambda book: book[1])

        answer = 0
        for book in book_ranges:
            a, b = book
            for i in range(a,b+1):
                if not visited[i]:
                    visited[i] = True
                    answer += 1
                    break
        print(answer)





