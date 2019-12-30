import operator
def majority_vote(lst):
    if lst == []:
        return None
    dic = {i:0 for i in lst}
    vte = list(dic)
    for i in vte:
        count = lst.count(i)
        dic.update({i:count})
    hv = max(dic.items(), key=operator.itemgetter(1))[0]
    av = len(lst)
    if dic[hv] > av / 2:
        return hv
    else:
        return None

majority_vote(["A", "A", "B"])