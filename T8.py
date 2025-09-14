import itertools
permutations = list(itertools.permutations(range(1, 10)))
count_permutations= len(permutations)
print(count_permutations)
count = 0
for [i1,i2,i3,i4,i5,i6,i7,i8,i9] in permutations:
    m = i1*100 + i2*10 + i3*1
    n = i4*100 + i5*10 + i6*1
    o = i7*100 + i8*10 + i9*1
    if m+n+o == 2025:
        count += 1
print(count)