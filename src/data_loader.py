import pandas as pd

class DataLoader:
    def __init__(self,original_csv,processed_csv):
        self.original_csv=original_csv
        self.processed_csv=processed_csv
        
    def loader_process(self):
        df=pd.read_csv(self.original_csv,encoding='utf-8').dropna()
        
        required_columns={"movie_name","year","runtime","genre","description","director","star"}
        
        missing=required_columns-set(df.columns)
        
        if missing:
            print("Column is not there in the original csv")
            
        df["movie_data"]=("movie_name:" + df['movie_name'] + " year:" + df['year'] + " runtime:" + df['runtime'] + " genre:" + df["genre"] + " description:" + df['description'] + " description:" + df['description'] + " director:" + df['director'] + " star:" + df['star'])
        
        df[['movie_data']].to_csv(self.processed_csv,index=False,encoding='utf=8')
        
        return self.processed_csv
    
        
        
        
        