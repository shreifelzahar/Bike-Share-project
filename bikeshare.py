import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        
        
        city = input("Please select the city that you want to explore chicago , new york city or washington in lower case \n").lower()
    
        if(city =="chicago" or city =="new york city" or city== "washington"):
            
            break
        else:
            
            print("you enter an invalid input please select one of these cities chicago , new york city or washington \n")
    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        
        
        month=input("Please select the month january , february ,march ,april ,may ,june or type all if u want to check all 6 months in lowercase \n ").lower()
        
        if (month =="january" or month =="february" or  month =="march" or month =="april" or month =="may" or month =="june" or month =="all"):
            
            break
        else:
            
            
            print("you entered an invalid input please select one of the monthesjanuary , February , march , april , may , june or type all if u want to check all 6 months \n ") 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        
        
        day=input("Please select the day that you want to filter monday , tuesday , wednesday , thursday , friday , saturday or type all if u want to check all the 7 days in lower case \n").lower()
        if(day =="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day =="friday" or day=="saturday" or day=="all"):
            
            break
        else:
            
            
            print("you entered an invalid inputPlease select the day that you want to filter monday , tuesday , wednesday , thursday , friday , saturday or type all if u want to check all the 7 days \n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month !="all" :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
    
    return df

def raw_data(df):
    #Asks the user if he/she want to display the first five row of the filterd data 
    row=0
    
    display=input("Do you want to display the first five rows of data yes or no \n").lower()
    while True:
        if(display=="yes"):
            print(df[row:row+5])
            print('-'*40)
                       
            display=input("Would you like to display the next five rows of data \n ")
            
            row+=5
        else:
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("the most common month according to the data you provide is : ",common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("the most common day according to the data you provide is : ", common_day)

    # TO DO: display the most common start hour
    common_start_hour =df["Start Time"].mode()[0]
    print("the most common hour according to the data you provide is : ",common_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df["Start Station"].mode()[0]
    print("The most common start sation according to the data give is : ",common_start_station) 

    # TO DO: display most commonly used end station 
    common_end_station =df["End Station"].mode()[0]
    print("The most common end sation according to the data give is : ",common_end_station) 


    # TO DO: display most frequent combination of start station and end station trip
    common_combination =df.groupby(["Start Station","End Station"]).size().idxmax()[0]
    print("Themost frequent combination of start station and end station trip according to the data give is : ",common_combination) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



            
    
    
    
    
    
    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("Trip duration in hours : ",total_travel_time/3600,"hour")


    # TO DO: display mean travel time
    mean_travel_time =df["Trip Duration"].mean()
    print("The average trip duration : ",mean_travel_time/3600,"hour")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
     # TO DO: Display counts of user types
  
    if "User Type" in df:
        user_types = df['User Type'].value_counts()
        print("The counts of user types : ",user_types,"\n")
        
   


    # TO DO: Display counts of gender
    if "Gender" in df:
        genders=df["Gender"].value_counts()
        print("the counts of genders :",genders,"\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_year = df["Birth Year"].min()
        print("The earliest year of birth is : ",earliest_year,"\n")
        most_recent_year = df["Birth Year"].max()
        print("The most recent year of birth is : ",most_recent_year,"\n")
        most_common_year=df["Birth Year"].mode()[0]
        print("The most common year of birth is : ",most_common_year,"\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
