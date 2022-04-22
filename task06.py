def maximum(p,q,s):
    if p>q and p>s:
        biggest = p

    elif q>p and q>s:
        biggest = q

    elif s>p and s>q:
        biggest = s
    return biggest

print(maximum(2,4,1))