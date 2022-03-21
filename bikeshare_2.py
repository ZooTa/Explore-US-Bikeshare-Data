import imp


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
keys = [k for k, v in CITY_DATA.items()]
days = ['friday', 'monday', 'saturday', 'sunday', 'thursday', 'tuesday', 'wednesday']
months = ['january', 'february', 'march', 'april', 'may', 'june']
filters = ['month', 'day', 'both', 'not at all', 'none']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = True
    dayB = True
    monthB = True
    filtB = True
    month, day = 'all','all'
    while city_name:
        city = input('Would you like to see data for Chicago, New York, or Washington?')

        if city in keys:
            city_name = False
            
        if city_name:
            print('I don\'t understand that')
    
    # get user input for month (all, january, february, ... , june)
    while filtB:
        
        filt = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.').lower()
        if filt in filters:
            filtB = False   
        
        if filtB:
            print('I don\'t understand that')             
    
    if filt == 'day':
       while dayB:
        
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
            if day in days:
                dayB = False
            
            if dayB:
                print('I don\'t understand that')
    
    elif filt == 'month':
        while monthB:
            
            month = input('Which month - January, February, March, April, May, or June?').lower()
            
            if month in months:
                monthB = False
                
            if monthB:
                print('I don\'t understand that')    
    elif filt == 'both':
        
        while dayB:
        
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
            if day in days:
                dayB = False
            
            if dayB:
                print('I don\'t understand that')
                
        while monthB:
            
            month = input('Which month - January, February, March, April, May, or June?').lower()
            
            if month in months:
                monthB = False
                
            if monthB:
                print('I don\'t understand that') 



    # get user input for day of week (all, monday, tuesday, ... sunday)


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df  


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    popular_month = df['month'].mode().iloc[0]
    popular_day = df['day'].mode().iloc[0]
    popular_hour = df['hour'].mode().iloc[0]




 
    
    # display the most common month
    print('the most pop month is',popular_month)

    # display the most common day of week
    print('the most pop day is',popular_day)

    # display the most common start hour
    print('the most pop hour is',popular_hour)   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode().iloc[0]
    print('most common start station', most_common_start_station)

    # display most commonly used end station
    most_common_start_station = df['End Station'].mode().iloc[0]
    print('most common end station',most_common_start_station)

    # display most frequent combination of start station and end station trip
    df['most common trip'] = df['Start Station'] +' to '+ df['End Station']  
    most_common_start_station = df['most common trip'].mode().iloc[0]
    print('most common trip',most_common_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    total_travel_time = df['Trip Duration'].sum()
    print('total travel time', total_travel_time)

    # display mean travel time


    average_travel_time = df['Trip Duration'].mean()
    print('average travel time', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    counts_of_each_user_type = df['User Type'].value_counts()
    sub = counts_of_each_user_type[0]
    cust = counts_of_each_user_type[1]


    print('counts of Subscriber is', sub)
    print('counts of Customer is', cust)


    # Display counts of gender
    if city in ['chicago','new york']:
        counts_of_each_gender = df['Gender'].value_counts()

        male = counts_of_each_gender[0]
        female = counts_of_each_gender[1]

        print('count of males', male)
        print('count of females', female)

    # Display earliest, most recent, and most common year of birth

        dfna = df.dropna(axis = 0)
        df['Birth Year'] = dfna['Birth Year']
        earleast_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode().iloc[0]

        print('earleast year is', earleast_year)
        print('most recent year is', most_recent_year )
        print('most common year is', most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
