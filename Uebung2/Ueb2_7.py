from main import *

print(data.index)
print(data['births'])
plt.hist(data['births'], density=1, bins=5478)
plt.show()