from connect import cursor, data_base

def creat_sorteio(table, sorteio, n1, n2, n3, n4, n5, n6):
    sql = f'''INSERT INTO {table}(idSorteio, n1, n2, n3, n4, n5, n6)
    values
    ({sorteio}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6})
    '''

    cursor.execute(sql)
    data_base.commit()