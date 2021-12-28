names = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((name, klass) for name, klass in zip(names,klasses))
print(next(gen))

from intertools import zip_longest

gen = ((nme, klass) for name, klass in zip_longest(names, klasses) if name is not None)
print(next(gen))