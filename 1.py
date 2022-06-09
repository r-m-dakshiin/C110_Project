import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

fr = ff.create_distplot([data], ["reading_time"], show_hist=False)
fr.show()

reading_time_mean = statistics.mean(data)
reading_time_std_deviation = statistics.stdev(data)

print("Reading Time Mean : ", reading_time_mean)
print("Reading Time Std Deviation : ", reading_time_std_deviation)




def random_set_of_mean(counter):
    data_Set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_Set.append(value)
    mean = statistics.mean(data_Set)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        random_means = random_set_of_mean(30)
        mean_list.append(random_means)
    show_fig(mean_list)

setup()
    


print(df['reading_time'])