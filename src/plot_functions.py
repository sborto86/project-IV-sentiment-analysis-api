## IMPORTING LIBRARIES AND SETTING PARAMETERS
import seaborn as sns
from matplotlib import pyplot as plt
if "pd" not in dir():
    import pandas as pd

sns.set_context('poster')
sns.set_style('whitegrid')

def sentiment_timeplot (df, y, group="name", filter=None, filename=None, width=16, heigh=9):
    '''
    Plots a sentiment value over time grouped by name, country or political party
    Arguments:
        df: df
            DataFrame in the specified format
        y: str. ("all", "polarity", "subjectivity", "neg", "neu", "pos", "compound")
            Sentiment metric to plot
        group: str. (Default: "name"), ("name", "country", "party")
            column name to be grouped by
        filter: list. (Default: None)
            list of terms to filter the dataframe y column before grouping
        width: int.
            figure width
        heigh: int.
            figure heigh
        filname: str. (Default: None)
            name of the file to be saved as png, if none the plot won't be saved
    '''
    sns.set(rc={'figure.figsize': (width, heigh)})
    ## Setting dataframe to timeseries
    df = df.set_index(df['date'])
    df.index = pd.DatetimeIndex(data=df.index)
    df = df.sort_index()
    ## preparing the dataframe to plot
    if filter:
        df = df[df[group].isin(filter)]
        if len(filter) == 1 and y=="all":
            fig_ = df[["polarity", "subjectivity", "neg", "neu", "pos", "compound"]].rolling('30.5D', min_periods=10).mean().plot()
        elif len(filter) == 1 and y != "all":
            fig_ = df[[y]].rolling('30.5D', min_periods=10).mean().plot()
    if y != "all":
        df = df.groupby(group)[y].rolling('30.5D', min_periods=10).mean().reset_index()
        ## Plotting
        fig_ = sns.lineplot(data=df, x='date', y=y, hue=group)
    if y == "neu":
        plt.ylim(0, 1)
    elif y !=all:
        plt.ylim(-0.5, 0.5)
    if y != all:
        plt.title(f"{y.capitalize()} Sentiment Score Over Time", fontsize = 25)
        plt.ylabel(f'{y.capitalize()} Score')
    else:
        plt.title(f"Sentiment Score Over Time", fontsize = 25)
        plt.ylabel(f'Score')
    ## Saving figure
    if filename:
        plt.savefig(f"./img/{filename}.png", dpi=1000)
    return plt.show(fig_)
    
def sentiment_boxplot(df, x='name', y ='compound', filter=None, width=16, heigh=9, filename=None):
    '''
    Plots a sentiment boxplot grouped by name, country or political party
    Arguments:
        df: df
            DataFrame in the specified format
        y: str. (Default: "compound") ("polarity", "subjectivity", "neg", "neu", "pos", "compound")
            Sentiment metric to plot
        x: str. (Default: "name"), ("name", "country", "party")
            column name to be grouped by
        filter: list. (Default: None)
            list of terms to filter the dataframe y column before grouping
        width: int.
            figure width
        heigh: int.
            figure heigh
    '''
    sns.set(rc={'figure.figsize': (width, heigh)})
        
    ## preparing the dataframe to plot
    if filter:
        df = df[df[x] in filter]
    fig_ = sns.boxplot(data=df, x=x, y=y)
    plt.title(f"{y.capitalize()} Sentiment Score", fontsize = 25)
    plt.ylabel(f'{y.capitalize()} Score')
    ## Saving figure
    if filename:
        plt.savefig(f"./img/{filename}.png", dpi=1000)
    return plt.show(fig_)