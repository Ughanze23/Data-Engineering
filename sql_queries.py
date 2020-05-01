# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays \
(songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP NOT NULL,\
user_id varchar REFERENCES users(user_id), level varchar NOT NULL,\
song_id varchar REFERENCES songs(song_id), \
artist_id varchar REFERENCES artists(artist_id), session_id int NOT NULL\
, location varchar NOT NULL, user_agent varchar NOT NULL)\
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id varchar PRIMARY KEY, first_name varchar NOT NULL, last_name varchar NOT NULL, gender varchar NOT NULL,level varchar NOT NULL,user_agent varchar NOT NULL)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar UNIQUE, artist_id varchar REFERENCES artists(artist_id),year int,duration int)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, artist_name varchar, location varchar NOT NULL, latitude float(6), longitude float(6))
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP NOT NULL, hour int, day int, week int, month int, year int, weekday int,session_id int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time,user_id,level,song_id,\
artist_id,session_id,location,user_agent) \
Values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users (user_id,first_name,last_name,gender,level,user_agent) Values (%s,%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration) Values(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id,artist_name,location,latitude,longitude) Values(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING """)


time_table_insert = ("""INSERT INTO time (start_time,hour,day,week,month,year,weekday,session_id) Values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""SELECT song_id,art.artist_id FROM songs JOIN artists art ON art.artist_id = songs.artist_id
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]