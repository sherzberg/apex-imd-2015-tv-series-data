import os

INSERT_FORMAT = '''
INSERT INTO episode
    (id, season, number_in_season, title, tv_series_id)
VALUES
    ({id}, {season}, {number_in_season}, "{title}", {j});

'''

series_data = open('data/series.csv', 'r').readlines()
series_data = [s.strip().split(",") for s in series_data[1:]]


for j, series in enumerate(series_data):
    series_name = series[0]
    series_id = series[1]

    file_name = 'data/' + series_id + '.csv'
    if not os.path.isfile(file_name):
        continue

    lines = open(file_name, 'r').readlines()

    inserts = '''
INSERT INTO tv_series
    (id, name)
VALUES
    ({j}, "{series_name}");

    '''.format(**locals())

    for i, line in enumerate(lines[1:]):
        split = line.strip().split(',')

        number = split[0].split('.')

        if len(number) != 2:
            continue

        id = i + 1000 * j
        season = number[0].strip()
        number_in_season = number[1].strip().replace('\xc2\xa0', '')
        title = split[1].strip()

        insert = INSERT_FORMAT.format(**locals())

        inserts += insert

    with open('sql/' + series_name.replace(' ', '_') + '.sql', 'w') as of:
        of.write(inserts)

