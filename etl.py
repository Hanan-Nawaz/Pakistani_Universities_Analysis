import pandas as pd
import mysql.connector

def extract():
    uni_pak = pd.read_csv("DataSets/uni.csv")
    uni_ranking = pd.read_csv("DataSets/ranking.csv")

    return [uni_pak, uni_ranking]

def transform(df_list):
    uni_pak = pd.DataFrame(df_list[0][["University Name", "Established Since", "Sector", "City", "Province"]])
    uni_pak["Established Since"] = pd.to_datetime(uni_pak["Established Since"])
    uni_pak['Established Since'] = uni_pak['Established Since'].dt.strftime('%Y-%m-%d')

    uni_pak.dropna()

    uni_ranking = pd.DataFrame(df_list[1][["2025 Rank", "2024 Rank", "Institution Name", "Location"]])
    uni_ranking_pak = uni_ranking.loc[uni_ranking["Location"] == "PK"]
    uni_ranking_pak.dropna()
    uni_ranking_pak.index = range(1, len(uni_ranking_pak) + 1)
    
    return [uni_pak, uni_ranking_pak]

def load(list):
    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hanan12335",
            database="Pak_Universities"
        )

        my_cur = conn.cursor()

        for index, rows in list[0].iterrows():
            my_cur.execute(
                "INSERT INTO Uni_list (Id, Name, Established_date, Sector, City, Province) VALUES (%s, %s, %s, %s, %s, %s)",
                (index + 1, rows["University Name"], rows["Established Since"], rows["Sector"], rows["City"], rows["Province"])
            )

        for index, rows in list[1].iterrows():
            my_cur.execute(
                "INSERT INTO Ranked_Uni_list (Id, Name, 2025_ranking, 2024_ranking) VALUES (%s, %s, %s, %s)",
                (index + 1, rows["Institution Name"], rows["2025 Rank"], rows["2024 Rank"])
            )

        conn.commit()
        print("ETL performed successfully.")

    except mysql.connector.Error as err:
        # Print error message and rollback transaction if an error occurs
        print(f"Error: {err}")
        conn.rollback()
    
    finally:
        conn.close()

df_list = extract()
uni_list_state = transform(df_list) 
load(uni_list_state)