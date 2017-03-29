def licenseKeyFormatting(S,K):
    pointer=len(S)-1
    out=''
    each_k=K
    while pointer >=0:
        if S[pointer]!='-':
            out=S[pointer].upper()+out
            if each_k==1:
                each_k=K
                if pointer!=0:
                    out='-'+out
            else:
                each_k-=1
        pointer-=1
    return out.strip('-')

print licenseKeyFormatting('2-4A0r7-4k',3)


