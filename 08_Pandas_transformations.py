# %% 
import pandas as pd
import numpy as np

df = pd.read_csv('./pokemon_data.csv')
df.head(3)

# %% 
# Calculate a new column
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
df.head(3)

# %%
# Filter dataframe

# masking
print(df[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")].head(1)
)

# using query function
# with @var can import in predicate variables
ids_list = ["Grass","Ivysaur"]
print(df.query(" `Type 1` == @ids_list ")[:5])

# using np.where
msk = np.where(df["Type 1"] == "Grass")
print(df.loc[msk][:5])

# %%
# sort dataframe 
df.sort_values(["Type 1", "Type 2"],ascending=[False,False])

# %%
# is not inplace function
df.drop(["Type 1", "Type 2"],axis=1).columns

