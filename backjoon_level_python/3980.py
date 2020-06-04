maximum_ability_maximum = 0

def solve(player_abilities):
    team_position_ability = [0] * SOCCER_PLAYER_NUM

    def dfs(depth):
        global maximum_ability_maximum
        if depth == SOCCER_PLAYER_NUM:
            maximum_ability_maximum = max(maximum_ability_maximum, sum(team_position_ability))
            return
        for i in range(SOCCER_PLAYER_NUM):
            if player_abilities[depth][i] != 0 and team_position_ability[i] == 0:
                team_position_ability[i] = player_abilities[depth][i]
                dfs(depth + 1)
                team_position_ability[i] = 0
    dfs(0)
    return maximum_ability_maximum


if __name__ == '__main__':
    C = int(input())
    SOCCER_PLAYER_NUM = 11
    for _ in range(C):
        player_availity = []
        maximum_ability_maximum = 0
        for i in range(SOCCER_PLAYER_NUM):
            player_availity.append(list(map(int, input().split())))
        print(solve(player_availity))
