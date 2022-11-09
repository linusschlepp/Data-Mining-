from main import pd, target, plt, features, data
import seaborn as sns

sns.set()
data = pd.DataFrame(data, columns=features)
data['iris'] = target
sns.pairplot(data, hue='iris', height=2.5)
plt.show()