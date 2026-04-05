def clean_data(df):
    df = df.copy()
    df = df[df['AveRooms'] < 10]
    return df