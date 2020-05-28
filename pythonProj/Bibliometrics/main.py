from dataReader import *
import numpy as np

import matplotlib as mpl
mpl.rc('axes',labelsize=10)
mpl.rc('xtick',labelsize=10)
mpl.rc('ytick',labelsize=10)
from itertools import permutations,combinations
import matplotlib.pyplot as plt
'''
save fig
'''
def saveFig(figid,img='images',extension='png',resolution=300,tight_layout=True):
    imgFolder=os.path.join(os.getcwd(),'images')
    if not os.path.exists(imgFolder):
        os.makedirs(imgFolder)
    imgFile=os.path.join(imgFolder,figid+'.'+extension)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(imgFile,format=extension,dpi=resolution)


'''
1. Read the data
'''
articles=readData('article_1_final_1.xlsx')
authors=readData('author_1_final.xlsx')
print('The shape of the article table is {}'.format(articles.shape))
print('The shape of the author table is {}'.format(authors.shape))
print('The number of unique authors is {}'.format(len(np.unique(authors['Author Name'].values))))

'''
2. Count the numbers of publcations and Citations each year
Merge the article and author table based on the article no.
fill the NA with 0
then group the merged table on the year and aggregate the citations and publications on that year
'''
mergedTable=authors.merge(articles,right_on=['Number'],left_on=['Article Number'],how='inner')

# observe the values in each field
# print(mergedTable.describe())
mergedTable.fillna(0,inplace=True)
# print(mergedTable.describe())

pub_citation_with_years=mergedTable.groupby(['Year']).apply(lambda x:pd.Series(dict(publicationCnt=x.Title.count(),
                                                                                    citationCnt=x.Citation.sum())))

print(pub_citation_with_years.head(11))

'''
3. plot the yearly publications and citations jointly

input:
    datadf: the dataframe about the yearly publications and citations
    width: bar width
'''
def plotBar(datadf=pub_citation_with_years,width=0.5):
    years=list(datadf.index.values)
    pubs_year=datadf.publicationCnt.values
    citations_year=datadf.citationCnt.values
    x=np.arange(len(years))

    fig,ax=plt.subplots(figsize=(12,5))

    rect_citation=ax.bar(x-width/2,citations_year,width,color='green',edgecolor='black',label='Yearly Citations')
    for rect in rect_citation:
        height=rect.get_height()
        print(height)
        plt.annotate('{}'.format(np.int32(height)),
                     xy=(rect.get_x()+rect.get_width()/2,height),
                     xytext=(0,3),
                     textcoords='offset points',
                     ha='center',
                     va='bottom',
                     zorder=2)
    ax.set_ylabel('Yearly citations',color='green')
    ax.tick_params(axis='y',labelcolor='green')
    ax.legend(loc='upper left')

    par = ax.twinx()
    rect_publication=par.bar(x+width/2,pubs_year,width,color='darkblue',edgecolor='black',label='Yearly Publications')
    for rect in rect_publication:
        height=rect.get_height()
        plt.annotate('{}'.format(np.int32(height)),
                     xy=(rect.get_x()+rect.get_width()/2,height),
                     xytext=(0,3),
                     textcoords='offset points',
                     ha='center',
                     va='bottom')
    par.set_ylabel('Yearly Publications',color='darkblue')
    par.tick_params(axis='y',color='darkblue')
    saveFig('Yearly_Publication_Citation')
    plt.show()

plotBar(pub_citation_with_years,width=0.5)

'''
4. predict the trends of yearly accumulated publications and citations
'''




