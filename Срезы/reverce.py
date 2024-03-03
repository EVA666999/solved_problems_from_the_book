def rev_f():
    a = 'Василе Николаевич Крецу'
    b = a.split()
    result = ''
    for i in b:
        result += i[0] + '.'
    return result


print(rev_f())