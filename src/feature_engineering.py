import numpy as np

def add_features(df):
    df = df.copy()
    df['RoomsPerPerson'] = df['AveRooms'] / df['Population']
    df['Population_log'] = np.log1p(df['Population'])
    return df