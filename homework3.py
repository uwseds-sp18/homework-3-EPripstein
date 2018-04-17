import pandas as pd
import sqlite3
import os

def create_dataframe(db_path):
    if not os.path.exists(db_path):
        raise ValueError('Provided file path is invalid')
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("""SELECT video_id, category_id, 'DE' AS language FROM DEvideos
                            UNION
                            SELECT video_id, category_id, 'CA' AS language FROM CAvideos
                            UNION
                            SELECT video_id, category_id, 'FR' AS language FROM FRvideos
                            UNION 
                            SELECT video_id, category_id, 'GB' AS language FROM GBvideos
                            UNION
                            SELECT video_id, category_id, 'US' AS language FROM USvideos;""", conn)
    return df