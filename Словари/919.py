phoneboock = {'Крис': '919-555-1111', 'Кэти': '828-111-111', 'Джо': '919-11-133', 'Д1о': '119-11-133'}
phoneboock_copy = {k:v for (k,v) in phoneboock.items() if v[:3] == '919'}
print(phoneboock_copy)