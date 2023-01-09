import psycopg2
import matplotlib.pyplot as plt

username = 'StudentKarachunA'
password = '2003'
database = 'db_lab2_Karachun'
host = 'localhost'
port = '5432'

query_1 = '''
DROP VIEW IF EXISTS GetCountriesStat;
CREATE VIEW GetCountriesStat AS
SELECT TRIM(countries.country_name) AS country, COUNT(wines.country_id) FROM wines 
JOIN countries ON countries.country_id = wines.country_id
GROUP BY country_name;
SELECT * FROM GetCountriesStat;
'''

query_2 = '''
DROP VIEW IF EXISTS GetPoints;
CREATE VIEW GetPoints AS
SELECT points AS points, COUNT(points) FROM wines 
GROUP BY points;
SELECT * FROM GetPoints;
'''

query_3 = '''
DROP VIEW IF EXISTS GetPriceStat;
CREATE VIEW GetPriceStat AS
SELECT TRIM(designation) AS designation, price FROM wines
ORDER BY price;
SELECT * FROM GetPriceStat;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()

# query_1
    cur.execute(query_1)
    country = []
    n_wines = []

    for row in cur:
        country.append(row[0])
        n_wines.append(row[1])

    x_range = range(len(country))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.bar(x_range, n_wines, label='Total')
    bar_ax.set_title('Amount of wine by each country')
    bar_ax.set_xlabel('Wines')
    bar_ax.set_ylabel('Amount of wines')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(country, rotation=45)

# query_2
    cur.execute(query_2)
    genres = []
    wines = []

    for row in cur:
        genres.append(row[0])
        wines.append(row[1])

    pie_ax.pie(wines, labels=genres, autopct='%1.1f%%')
    pie_ax.set_title('Points (in percent)')

# query_3
    cur.execute(query_3)
    title = []
    prices = []

    for row in cur:
        title.append(row[0])
        prices.append(row[1])

    graph_ax.plot(title, prices, marker='o')
    graph_ax.set_xlabel('Wines')
    graph_ax.set_ylabel('Price')
    graph_ax.set_title('A prices of wine')
    graph_ax.set_xticklabels(title, rotation=40)

    for qnt, price in zip(title, prices):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(1400, 750)

plt.subplots_adjust(left=0.1, bottom=0.19, right=0.94, top=0.9, wspace=0.4, hspace=0.4)

plt.show()

