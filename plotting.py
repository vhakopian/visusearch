import dataset_extraction
import matplotlib.pyplot as plt

def plot(dataframe):


    fig = plt.figure(figsize=(14, 1))
    
    axWeek = plt.subplot(221)
    plt.title("Number of searches by week", fontsize=14, ha="center") 
    
    axMonth = plt.subplot(222)
    plt.title("Number of searches by month", fontsize=14, ha="center") 
    
    axWordPerWeek = plt.subplot(223)
    plt.title("Average number of words by query by week", fontsize=14, ha="center") 
    
    axWordPerMonth = plt.subplot(224)
    plt.title("Average number of words by query by month", fontsize=14, ha="center") 
    
    
    fig.patch.set_facecolor('white')
    
    
    axWeek.plot(dataframe["numberQuery"].resample("W").sum())
    axMonth.plot(dataframe["numberQuery"].resample("M").sum())
    axWordPerWeek.plot(dataframe["numberWords"].resample("1W").mean())
    axWordPerMonth.plot(dataframe["numberWords"].resample("M").mean())

def main():
    dataframe = dataset_extraction.load_dataset()
    plot(dataframe)
    
if __name__ == "__main__":
    main()