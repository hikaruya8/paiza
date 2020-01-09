n=int(input())
string_list=[input() for i in range(n)]

changed_list = []
for s in string_list:
    if s[-1] == 's' or 'o' or 'x':
        s_changed = s + 'es'

    elif s[-1] == 'y' and (s[-2] is not ('a' or 'i' or 'u' or 'e' or 'o')):
        s_changed = s + 'ies'

    elif s[-2:] == 'sh' or 'ch':
        s_changed = s + 'es'

    elif s[-1] == 'f':
        s_changed = s[:-1] + 'ves'

    elif s[-2:] == 'fe':
        s_changed =s[:-2] + 'ves'

    else:
        s_changed = s + 's'

    changed_list.append(s_changed)

for c in changed_list:
    print(c)