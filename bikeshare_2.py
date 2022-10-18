import time
import pandas as pd
import numpy as np
#another changes
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
    city  = input('Please enter the city name ').lower()
#     print(list(CITY_DATA.keys()))
    print(city in list(CITY_DATA.keys()))

    while city not in list(CITY_DATA.keys()):
        city  = input('Please enter the city name ').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)

    

    print('Enter the month want to analyze the data for: january, february, march, april, may, june')
    month = input("Please enter the month: ").lower()
    while month not in ['all','jan', 'feb', 'mar', 'apr', 'may', 'jun']:
        print('Invalid month select correct month!')
        month = input("choose jan, feb, mar, apr, may, jun: ").lower()

    


#     if month != 'all':
#         data = data[data['month']==months[month]]

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    
#     print(data)
    print('Enter the day you want to analyze the data for: monday, tuesday, wednesday, thrusday, friday, saturday, sunday')
    day = input("Please enter the day: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']:
        day = input('choose a weekday: ').lower()
#     if day != 'all':
#         data = data[data['day'] == day.title()]
#         print(city, month, day)


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
    df = pd.read_csv(CITY_DATA[city])  
    
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    if month != 'all':
        months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6}
        df = df[df['month']==months[month]]
    df ['day'] = pd.DatetimeIndex(df['Start Time']).day_name()    
    if day != 'all':
        df = df[df['day'] == day.title()]
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].value_counts().idxmax()
    print('common month was: ',common_month)

    # TO DO: display the most common day of week

    common_day =df['day'].value_counts().idxmax()
    print('common day was: ',common_day)
    # TO DO: display the most common start hour
    df['Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    common_hour =df['Hour'].value_counts().idxmax()
    print('common hour was: ',common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
#     df['start_route'] = df['Start Station']
    start_route=df['Start Station'].value_counts().idxmax()
    print('Most common start station was: ', start_route)

    # TO DO: display most commonly used end station
#     df['end_route'] = df['End Station']
    end_route=df['End Station'].value_counts().idxmax()
    print('Most common end station was: ', end_route)

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_route'] = df['Start Station'] +' -> '+df['End Station']
    common_route=df['frequent_route'].value_counts().idxmax()
    print('Most common route was: ', common_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time was ',df['Trip Duration'].sum())

    # TO DO: display mean travel time

    print('Average travel time was ',df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts().to_dict()
    print(counts)
    
    # TO DO: Display counts of gender
    if city == 'washington':
        print('Skip gender and birth year analysis')
    else:    
        
        gen_cnt = df['Gender'].value_counts().to_dict()
        print(gen_cnt)

        mbr_year = df['Birth Year'].min()
        print('earliest birth year: ',mbr_year)

        maxbr_year = df['Birth Year'].max()
        print('Most recent birth year: ',maxbr_year)

        cbr_year = df['Birth Year'].value_counts().idxmax()
        print('most common birth year: ',cbr_year)



        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        inputs=input('Would you like to print the first five rows of data? ')
        rows = 0
        while inputs != 'no':

            print(df.iloc[rows:rows+5])
            rows = rows +5
            # rows += 5
            inputs=input('Would you like to print the first five rows of data? Enter Yes or No.\n' )

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
