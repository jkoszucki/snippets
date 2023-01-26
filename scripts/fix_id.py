def fix_id(r):
    if 'nan' in r.id:
        return r.id.replace('nan', '2665')
    one, two ,three, four = r.id.split('_')
    three = three.replace('.0', '')
    return '_'.join([one, two ,three, four])


def fix_name(r):
    if 'nan' in r.name:
        return r.name.replace('nan', '2665')
    one, two ,three, four = r.name.split('_')
    three = three.replace('.0', '')
    return '_'.join([one, two ,three, four])
