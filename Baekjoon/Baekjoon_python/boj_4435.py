#중간계 전쟁
import sys
t = int(sys.stdin.readline().rstrip())

for i in range(1, t + 1):
    gandalf = list(map(int, sys.stdin.readline().rstrip().split()))
    saruman = list(map(int, sys.stdin.readline().rstrip().split()))

    g_res = gandalf[0] * 1 + gandalf[1] * 2 + gandalf[2] * 3 \
            + gandalf[3] * 3 + gandalf[4] * 4 + gandalf[5] * 10
    s_res = saruman[0] * 1 + saruman[1] * 2 + saruman[2] * 2 \
            + saruman[3] * 2 + saruman[4] * 3 + saruman[5] * 5 + saruman[6] * 10

    print(f'Battle {i}: ', end='')
    if g_res > s_res:
        print('Good triumphs over Evil')
    elif g_res < s_res:
        print('Evil eradicates all trace of Good')
    else:
        print('No victor on this battle field')