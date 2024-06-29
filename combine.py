import pandas as pd
import glob
import os
directory = 'C:/Users/mstut/desktop/Python/Movies Dataset/dataset/1_movies_per_genre'
file_pattern = os.path.join(directory, '*.csv')
csv_files = glob.glob(file_pattern)
df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index = True)
output_file = 'C:/Users/mstut/desktop/Python/Movies Dataset/combined.csv'
df.to_csv(output_file, index = False)
print(f"Combined {len(csv_files)} CSV files into {output_file}")