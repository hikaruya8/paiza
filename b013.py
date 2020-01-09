a,b,c =  map(int, input().split())
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

oriru_time = 539-(b+c)
densha_jikoku = [(t[0]*60)+t[1] for t in time]

machi_jikan = [(oriru_time-d) for d in densha_jikoku if (oriru_time-d) >= 0]
noru_densha = machi_jikan.index(min(machi_jikan))
deru_jikan = time[noru_densha][0]*60 + time[noru_densha][1]-a
nanji_deru = deru_jikan//60
nanhun_deru = deru_jikan%60
print('0{}:{}'.format(nanji_deru, nanhun_deru))