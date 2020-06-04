def solve(N, guilts, matrix):

    def dfs(num_people_left, night_count):
        global maximum_night_count
        maximum_night_count = max(maximum_night_count, night_count)

        # 낮
        day_flag = False
        if num_people_left % 2 != 0:
            day_flag = True

            maximum_guilt_idx = -1
            temp_max = -1
            for idx, guilt in enumerate(guilts):
                if visited[idx] is False and guilt > temp_max:
                    temp_max = guilt
                    maximum_guilt_idx = idx

            if maximum_guilt_idx == Eunjin:
                return

            # kill maximum_guilt_idx
            visited[maximum_guilt_idx] = True
            num_people_left -= 1
        # 밤
        for i in range(N):
            if i != Eunjin and visited[i] is False:
                visited[i] = True # Kill Person i
                num_people_left -= 1

                # 다른 참가자 j의 유죄 지수는 R[i][j]만큼 변한다.
                for j in range(len(guilts)):
                    guilts[j] += matrix[i][j]

                dfs(num_people_left, night_count + 1)

                for j in range(len(guilts)):
                    guilts[j] -= matrix[i][j]
                visited[i] = False
                num_people_left += 1

        # 재귀 끝날때 낮에 죽은사람 다시 살려야함
        if day_flag:
            visited[maximum_guilt_idx] = False
            num_people_left += 1

    dfs(N, 0)
    return maximum_night_count

if __name__ == '__main__':
    N = int(input())
    visited = [False] * N

    guilts = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    Eunjin = int(input())

    maximum_night_count = 0

    print(solve(N, guilts, matrix))
    # solve(4, [500]*4, [[1,4,3,-2],[-2,1,4,3],[3,-2,1,4],[4,3,-2,1]])