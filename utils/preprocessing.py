import pandas as pd

df_train = pd.read_csv("../train.csv")

new_rows = []

# Iterate over the DataFrame rows
for index, row in df_train.iterrows():
    if row['winner_model_a'] == 1 or row['winner_tie'] == 1:
        new_row = row.copy()
        new_row['prompt'] = row['response_a']
        new_row['response_a'] = row['prompt']
        new_rows.append(new_row)
    if row['winner_model_b'] == 1 or row['winner_tie'] == 1:
        new_row = row.copy()
        new_row['prompt'] = row['response_b']
        new_row['response_b'] = row['prompt']
        new_rows.append(new_row)

# Create a DataFrame from the new rows
new_df = pd.DataFrame(new_rows)

df_expanded = pd.concat([df_train, new_df], ignore_index=True)
df_expanded.to_csv("train_reversal.csv", index=False)
