import pandas as pd
import datetime as dt

def extract():
    uni_pak = pd.read_csv("DataSets/uni.csv")
    uni_ranking = pd.read_csv("DataSets/ranking.csv")

    return [uni_pak, uni_ranking]

def transform(df_list):
    uni_pak = pd.DataFrame(df_list[0][["University Name", "Established Since", "Sector", "City", "Province"]])
    uni_pak["Established Since"] = pd.to_datetime(uni_pak["Established Since"])
    uni_pak.dropna()


    uni_ranking = pd.DataFrame(df_list[1][["2025 Rank", "2024 Rank", "Institution Name", "Location"]])
    uni_ranking_pak = uni_ranking.loc[uni_ranking["Location"] == "PK"]
    uni_ranking_pak.dropna()
    uni_ranking_pak.index = range(1, len(uni_ranking_pak) + 1)

    return [uni_pak, uni_ranking_pak]

def load(list):

    return 0

df_list = extract()
uni_list_state = transform(df_list) 
