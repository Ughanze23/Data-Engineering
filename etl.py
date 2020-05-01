import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """process song data and load them into artist and song tables """
    
    # open song file
    df = pd.read_json(filepath,lines=True)
    
     # insert artist record
    artist_data = list(df[['artist_id','artist_name','artist_location','artist_longitude','artist_longitude'\
                 ]].values[0])
    cur.execute(artist_table_insert, artist_data)

    # insert song record
    song_data = list(df[['song_id','title','artist_id','year','duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
     
    


def process_log_file(cur, filepath):
    """process Log data and load them into User and time tables """
    
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df.page == 'NextSong'] 

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], errors='coerce' ,unit = 'ms')
    df['ts'] = t
    
    # insert time data records
    time_data = (t.values.tolist()[0],t.dt.hour.values.tolist()[0],t.dt.day.values.tolist()[0],t.dt.weekofyear.values.tolist()[0],t.dt.month.values.tolist()[0]\
             ,t.dt.year.values.tolist()[0],t.dt.weekday.values.tolist()[0],df['sessionId'].values.tolist()[0])
   
    #set colum lables of time_table
    column_labels = ('Start time','hour','day','week of year','month','year','weekday','sessionid')
    
    # Create time_table dataframe
    time_df = pd.DataFrame([time_data],columns=column_labels)
    
    #covert column start time back to timestamp
    time_df['Start time'] = pd.to_datetime(time_df['Start time'])

    #insert records into time table
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level','userAgent']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()