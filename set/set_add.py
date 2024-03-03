"""ADD"""
my_Set = set()
my_Set.add(1)
"""UPDATE"""
q_set = set([1, 2, 3])
q_set.update([4, 5, 6])
"""DELITE"""
del_set = set([1, 2, 3])
del_set.discard(1)
"""CLEAR"""
clear_set = set([1, 2, 3])
clear_set.clear()
"""UNION or____ |  объединение"""
union_set = set([1, 2, 3])
union_set1 = set([4, 5, 3])
union_set2 = union_set.union(union_set1)
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1 | set2
"""Пересичение множеств intersection or____ &  и там и там есть """
int_set = set([1, 2, 3])
int_set2 = set([3, 4, 5])
int_set3 = int_set.intersection(int_set2)
"""Разность все елементы set1 которых нет в set2 or_____ -"""
dif_set = set([1, 2, 3, 4])
dif_set1 = set([3, 4, 5, 6])
dif_set2 = dif_set1.difference(dif_set)
dif_set3 = dif_set - dif_set1
"""Симетричноя разность это множестава которое содержит элементы
    не принадлижащие обоим множеставам ___________ которых нет не там не там or______ ^ """
sym_dif = set([1, 2, 3])
sym_dif1 = set([2, 1, 6])
sym_dif2 = sym_dif.symmetric_difference(sym_dif1)
sym_dif3 = sym_dif ^ sym_dif1
""""Одно из множеств содержит все элементы другого множества or_____ <=.
    Определение является ли одно из множеств надмножеством or _____ >="""
same_set = set([1, 2, 3, 4])
same_set1 = set([1, 2])
same_set2 = same_set1.issubset(same_set) # a содержит все элементы b
same_set3 = same_set1.issuperset(same_set1) # хз чо это 


baseball = set(['John', 'Karmen', 'Aida', 'Alisea'])
basketball = set(['Eva', 'Karmen', 'Alisea', 'Sara'])

def intersection():
    result = baseball.intersection(basketball)
    return result

def union():
    result = basketball.union(baseball)
    return result

def difference():
    result = baseball - basketball
    result = baseball.difference(basketball)
    return result


def dif2():
    result = basketball - baseball
    result = basketball.difference(baseball)
    return result


def sim_dif():
    result = baseball.symmetric_difference(basketball)
    return result

print(sim_dif())
