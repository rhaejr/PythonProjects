import pickle

with open('db.p', 'rb') as f:
    db = pickle.load(f)
    print('pickle')


def select_from_dict(db, items=(), conditions=()):
    # select item(s) from db with conditions or whole db
    if type(items) == str:
        items = (items,)
        print(items)

    if len(items) == 0:
        print('all')
        items = tuple(db[tuple(db.keys())[0]].keys())
        return select_from_dict(db, items, conditions)

    else:
        results = []
        for key in db:
            temp = []
            for item in items:
                meets_conditions = True
                for condition in conditions:
                    if db[item][condition[0]] != condition[1]:
                        meets_conditions = False
                if meets_conditions:
                    temp.append(db[key][item])
            results.append(temp)
        return results

print(select_from_dict(db,'pn', (('acft', 'apache'), ('pn', '7-511527009-101'))))
