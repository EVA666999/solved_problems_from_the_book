ms = set([1, 2, 3, 4])
ms1 = set([2, 3, 6, 7])
ms2 = ms.intersection(ms1)
ms3 = ms.difference(ms1)
ms4 = ms1.symmetric_difference(ms)  
print(ms4)