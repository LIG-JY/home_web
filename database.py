import pandas as pd

def save(location, cleaness, built_in):  #dataframe으로 데이터를 저장하는 함수
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"location":location,
                           "cleaness":cleaness,
                           "built_in":built_in}, 
                         index = [idx])
    new_df.to_csv("database.csv",mode = "a", header = False)
    return None

def load_list():  # 저장된 데이터를 리스트형태로 불러오는 함수
    house_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    # return house_list
    
def now_index():  
    df = pd.read_csv("database.csv")
    return len(df)-1


def load_house(idx):
    df = pd.read_csv("database.csv")
    house_inf = df.iloc[idx]
    return house_info


if __name__ =="__main__":
    load_list()