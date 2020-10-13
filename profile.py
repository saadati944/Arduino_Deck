def load(path):
    lines={'global':['']}
    pointer='global'
    file=open(path,'r')
    for ln in file.readlines():
        if ln[-1]=='\n':
            ln=ln[:-1]
        if ln=='' or ln.startswith('#'):
            continue
        elif ln=='>':
            pointer='global'
        elif ln.startswith('>') and len(ln)==2:
            pointer=ln[1:]
        elif ln.startswith('>') and len(ln)!=2:
            lines['port']=ln[1:]
        else:
            if pointer in lines:
                lines[pointer].append(ln)
            else:
                lines[pointer]=[ln]
    return lines