import pandas as pd
import mysql.connector

def extract():
    uni_pak = pd.read_csv("DataSets/uni.csv")

    return uni_pak

def transform(df):
    uni_pak = pd.DataFrame(df[["University Name", "Established Since", "Sector", "City", "Province"]])
    uni_pak["Established Since"] = pd.to_datetime(uni_pak["Established Since"])
    uni_pak['Established Since'] = uni_pak['Established Since'].dt.strftime('%Y-%m-%d')

    uni_pak.dropna()
    
    return uni_pak

def load(uni_pak):
    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hanan12335",
            database="Pak_Universities"
        )

        my_cur = conn.cursor()

        for index, rows in uni_pak.iterrows():
            my_cur.execute(
                "INSERT INTO Uni_list (Id, Name, Established_date, Sector, City, Province) VALUES (%s, %s, %s, %s, %s, %s)",
                (index + 1, rows["University Name"], rows["Established Since"], rows["Sector"], rows["City"], rows["Province"])
            )

        conn.commit()
        print("ETL performed successfully.")

    except mysql.connector.Error as err:
        # Print error message and rollback transaction if an error occurs
        print(f"Error: {err}")
        conn.rollback()
    
    finally:
        conn.close()

uni_pak_df = extract()
uni_pak_df_cleaned = transform(uni_pak_df) 
load(uni_pak_df_cleaned)