import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('teacher_bot.db')
    cur = base.cursor()
    '''
    if base:
        base.execute('CREATE TABLE IF NOT EXISTS students(stu_id INTEGER PRIMARY KEY , stu_name TEXT , stu_description TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS parents(par_id INTEGER PRIMARY KEY , par_stu_id INTEGER, par_name TEXT, par_description TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS schedule(sch_id INTEGER PRIMARY KEY , sch_stu_id INTEGER, sch_day TEXT, sch_time_start TEXT, sch_time_end TEXT, price TEXT, sch_reminder INTEGER)')
        base.execute('CREATE TABLE IF NOT EXISTS dz(dz_id INTEGER PRIMARY KEY , dz_stu_id INTEGER, dz_description TEXT, dz_img TEXT, dz_date TEXT, dz_done INTEGER, dz_done_ing TEXT)')
        # AUTOINCREMENT
        base.commit()
        # sql_proba_db()
        print('Data base connected OK')
    '''
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read_sch():
    str_request = 'SELECT stu_name as name, sch_day,  sch_hour_start, sch_min_start, sch_hour_end, sch_min_end,' \
                  ' sch_reminder,stu_tg_id FROM students, schedule WHERE stu_id=sch_stu_id ORDER BY name'
    return cur.execute(str_request).fetchall()

async def sql_read_dz():
    str_request = 'SELECT stu_name as name, dz_description, dz_img FROM students, dz ' \
                  'WHERE stu_id=dz_stu_id AND dz_done = 0 ORDER By name'
    return cur.execute(str_request).fetchall()
        # await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

'''
def sql_proba_db():
    student = [1, 'Иванов Иван', '5 класс. Помощь по школьной программе']
    parents = [
        [1,1, 'Иванова Наталья Александровна', 'Может говорить с 17.00 до 18.00 в рабочие дни'],
        [2, 1, 'Иванов Сергей Борисович', ''],
        [3, 1, 'Васильева Анна Витальевна', 'бабушка']
    ]
    schedules = [
        [1,1,'Понедельник', '18:00', '18:50', '2000','1'],
        [2, 1, 'Пятница', '19:00', '19:50', '2000', '1']
    ]
    dzs =[
        [1,1,'Рабочая тетрадь стр. 154','','2023-02-01',1,'' ],
        [2,1,'Рабочая тетрадь стр. 155','','2023-02-04',0,'' ],
        [3,1, 'Учебник № 112', '', '2023-02-10',0,'']
    ]
    cur.execute('INSERT INTO students VALUES (?, ?, ?)', tuple(student))
    for schedule in schedules:
        cur.execute('INSERT INTO schedule VALUES (?, ?, ?,?,?,?,?)', tuple(schedule))
    for parent in parents:
        cur.execute('INSERT INTO parents VALUES (?, ?, ?,?)', tuple(parent))
    for dz in dzs:
        cur.execute('INSERT INTO dz VALUES (?, ?, ?,?,?,?,?)', tuple(dz))
    base.commit()

    student = [2, 'Давид Демирчян', '8 класс. Курс "Дроби"']
    parents = [
         [4,2, 'Демирчян Людмила', 'мама'],
    ]
    schedules = [
        [3,2,'Вторник', '15:00', '15:50', '2000','0'],
        [4, 2, 'Четверг','19:00', '19:50', '2000', '0']
    ]
    dzs =[
        [4,2,'Рабочая тетрадь стр. 154','','2023-02-01',1,'' ],
        [5,2,'Рабочая тетрадь стр. 155','','2023-02-04',1,'' ],
        [6,2, 'Учебник № 112', '', '2023-02-10',0,'']
    ]
    cur.execute('INSERT INTO students VALUES (?, ?, ?)', tuple(student))
    for schedule in schedules:
        cur.execute('INSERT INTO schedule VALUES (?, ?, ?,?,?,?,?)', tuple(schedule))
    for parent in parents:
        cur.execute('INSERT INTO parents VALUES (?, ?, ?,?)', tuple(parent))
    for dz in dzs:
        cur.execute('INSERT INTO dz VALUES (?, ?, ?,?,?,?,?)', tuple(dz))
    base.commit()
'''
