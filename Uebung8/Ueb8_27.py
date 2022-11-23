from main import pd, DecisionTreeClassifier, plt, plot_tree

weather_df = pd.read_csv('weather.csv', header=0, sep=';', index_col='Weekend' )

weather_dict = {"Sunny":1, "Windy":2, "Rainy":3}
weather_df.Weather = [weather_dict[item] for item in weather_df['Weather']]
weather_df['Parents'] = weather_df['Parents'] == 'Yes'
weather_df['Money'] = weather_df['Money'] == 'Rich'
print(weather_df)

# Get first but last column in dataframe
df = weather_df.iloc[:,:-1]

# Get last column of dataframe
decision = weather_df.iloc[:,-1]

print(decision)

model = DecisionTreeClassifier(criterion='entropy', splitter='best')

model.fit(df, decision)

fig = plt.figure(num='Cinema', figsize=(10, 8))
plot_tree(model, feature_names=df.columns, filled=True, rounded=True)
plt.show()
