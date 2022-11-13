from main import *


def cluster(amount_clusters, different_algorithm=False):
    if different_algorithm:
        calculation = KMeans(n_clusters=amount_clusters, algorithm='elkan', init='random')
    else:
        calculation = KMeans(n_clusters=amount_clusters)

    calculation.fit(data)

    labels = calculation.labels_
    print(labels)
    print(target)
    color_lst = ['blue', 'cyan', 'green', 'yellow', 'pink', 'red', 'orange', 'grey', 'purple']
    image = plt.figure(num='irisdaten', figsize=(12, 4))
    content_1 = image.add_subplot(121)
    for index in range(amount_clusters):
        content_1.scatter(df[labels == index].petallength, df[labels == index].petalwidth, c=color_lst[index], s=25,
                          label='Cluster ' + str(index))
        # Add average
        content_1.scatter(df[labels == index].petallength.mean(), df[labels == index].petalwidth.mean(), c='black', s=25,
                          label='Average ' + str(index))

    content_1.set_title('Calculated with k-means')
    content_1.axis([0, 8, 0, 4])
    content_1.legend()
    content_1.set_xlabel('petallength')
    content_1.set_ylabel('petalwidth')

    content_2 = image.add_subplot(122)

    content_2.scatter(df[target == 0].petallength, df[target == 0].petalwidth, c='b', s=25, label='Setosa')
    print(calculation.n_iter_)
    plt.show()
