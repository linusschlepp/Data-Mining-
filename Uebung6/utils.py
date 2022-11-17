from main import data, KMeans, plt, df


def cluster(amount_clusters, different_algorithm=False):
    if different_algorithm:
        calculation = KMeans(n_clusters=amount_clusters, algorithm='elkan', init='random')
    else:
        calculation = KMeans(n_clusters=amount_clusters)

    calculation.fit(data)

    labels = calculation.labels_
    color_lst = ['blue', 'cyan', 'green', 'yellow', 'pink', 'red', 'orange', 'grey', 'purple']
    image = plt.figure(num='irisdata', figsize=(12, 4))
    content_1 = image.add_subplot(121)
    for index in range(amount_clusters):
        content_1.scatter(df[labels == index].petallength, df[labels == index].petalwidth, c=color_lst[index], s=25,
                          label='Cluster ' + str(index))
        # Add average
        content_1.scatter(df[labels == index].petallength.mean(), df[labels == index].petalwidth.mean(), c='black', s=25)

    content_1.set_title('Calculated with k-means')
    content_1.axis([0, 8, 0, 4])
    content_1.legend()
    content_1.set_xlabel('petallength')
    content_1.set_ylabel('petalwidth')

    print('Amount of iterations: {} for clusters: {}'.format(calculation.n_iter_, amount_clusters))
    plt.show()
