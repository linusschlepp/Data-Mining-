from main import data, pd, plt, y_column, x_columns, y


#TODO: Fix colorissue
grr = pd.plotting.scatter_matrix(data[y_column + x_columns], figsize=(15, 15), c='red', marker='o', s=30, alpha=0.8)

plt.show()
