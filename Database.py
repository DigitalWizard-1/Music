import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:qwert@localhost:5432/py46database')
connection = engine.connect()

Singer = ['Гражданская оборона', 'Алиса', 'Ария', 'КИНО', 'Радиотранс', 'Браво', 'МАЧЕТЕ', 'Михаил Кргу']
Genre = ['Рок', 'Поп', 'Шансон', 'Панк', 'Бит', 'Транс', 'Хеви-метал']
Alboum = [['Песни радости и счастья', 1990], ['Сейчас позднее, чем ты думаешь', 2003], ['С кем ты?', 1986], ['Звезда по имени солнце', 1989],
          ['Через терни к звездам', 2018], ['Московский бит', 1993], ['Мачете', 2012], ['Кольщик', 2009]]
Track = [['Все идет по плану', 290, 1], ['Так закалялась сталь', 146, 1], ['Небо славян', 275, 2], ['Воля и  разум', 274, 3],
         ['Встань, страх преодолей', 256, 3], ['Звезда по имени Солнце', 225, 4], ['Пачка сигарет', 268, 4], ['Печаль', 331, 4],
         ['Земля в огне', 307, 5], ['Космонавт', 331, 5], ['мой Ледяной мир', 293, 5], ['Стильный оранжевый галстук', 203, 6],
         ['Как жаль', 219, 6], ['Нежность', 290, 7], ['Кольщик', 287, 8]]
Sbornik = [['Золото шансона', 2015], ['Русский рок', 2019], ['Хиты 90-х', 2001], ['Кислотный Транс', 2002],
           ['Музыка 2000-х', 2014], ['Старое, но не забытое', 2001], ['Лучшие песни', 2018], ['Разное', 2021]]


for id in Genre:
    connection.execute(f"INSERT INTO genre(title) VALUES('{id}');")

for id in Singer:
    connection.execute(f"INSERT INTO singer(name_singer) VALUES('{id}');")

for id in Sbornik:
    connection.execute(f"INSERT INTO sbornik(name_sbornik, year_sbornik) VALUES('{id[0]}', {id[1]});")

for id in Alboum:
    connection.execute(f"INSERT INTO album(name_album, year_album) VALUES('{id[0]}', {id[1]});")

for id in Track:
    connection.execute(f"INSERT INTO track(name_track, duration, album_id) VALUES('{id[0]}', {id[1]}, {id[2]});")

connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(4, 1);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(1, 2);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(7, 3);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(1, 4);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(6, 5);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(5, 6);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(2, 7);")
connection.execute("INSERT INTO ge_si_buffer(genre_id, singer_id) VALUES(3, 8);")

connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(1, 1);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(2, 2);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(3, 3);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(4, 4);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(5, 5);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(6, 6);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(7, 7);")
connection.execute("INSERT INTO si_al_buffer(album_id, singer_id) VALUES(8, 8);")

connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(1, 8);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(2, 1);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(2, 2);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(2, 3);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(2, 4);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(3, 6);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(3, 7);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(3, 8);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(3, 12);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(3, 13);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(4, 9);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(4, 10);")
connection.execute("INSERT INTO sb_tr_buffer(sbornik_id, track_id) VALUES(4, 11);")

sel = connection.execute("""SELECT name_album, year_album FROM album
                            WHERE year_album=2018;""").fetchall()
print('Альбомы вышедшие в 2018 году:')
for id in sel:
    print(id[0],', ',id[1])
print()

sel = connection.execute("""SELECT name_track, duration FROM track
                            ORDER BY duration DESC;""").fetchone()
print('Самый длинный трек:\n', sel[0],', ',sel[1],'сек.')
print()

sel = connection.execute("""SELECT name_track, duration FROM track
                            WHERE duration>=210;""").fetchall()
print('Треки длиннее 3,5 минут:')
for id in sel:
    print(id[0],', ',id[1],'сек.')
print()

sel = connection.execute("""SELECT name_sbornik FROM sbornik
                            WHERE year_sbornik BETWEEN 2018 AND 2020;""").fetchall()
print('Сборники за 2018-2020 года:')
for id in sel:
    print(id[0])
print()

sel = connection.execute("""SELECT name_singer FROM singer
                            WHERE name_singer NOT LIKE '%% %%';""").fetchall()
print('Имена исполнителей из одного слова:')
for id in sel:
    print(id[0])
print()

sel = connection.execute("""SELECT name_track FROM track
                            WHERE name_track LIKE '%%my%%' OR name_track LIKE '%%мой%%';""").fetchall()
print('Название треков с мой/my:')
for id in sel:
    print(id[0])
print()
