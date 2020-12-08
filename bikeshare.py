import time
import pandas as pd
import numpy as np
from colorama import Fore, Style

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
    while True:
        city = input('which city would you like to explore? (chicago, new york city, washington): ').lower()
        if  city not in ['chicago', 'new york city', 'washington']:
            print(Fore.RED +'**please choose one of these cities: (chicago, new york city, washington), try again.**\n'+ Style.RESET_ALL)
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWould you like to filter the data by a specific month? if yes, please choose one ( January, February, March, April, May, June), if no enter 'all' please: ").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print(Fore.RED + '**Please enter a valid input, try again.**\n' + Style.RESET_ALL)
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWould you like to filter the data by a specific day? if yes, please choose one ( Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), if no enter 'all' please: ").lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print(Fore.RED + '**Please enter a valid input, try again.**\n' + Style.RESET_ALL)
            continue
        else:
            break


    print('-'*40)
    return city, month, day

#------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month: {}'.format(popular_month))


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day of week: {}'.format(popular_day))


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['Start Hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Stations'] = 'From: ' + df['Start Station'] + ', To: ' + df['End Station']
    popular_trip_stations = df['Trip Stations'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip: {}'.format(popular_trip_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#------------------------------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The total mean time is {}".format(mean_travel_time) )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-------------------------------------------------------------------------------------------------

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The Types of Users Bikeshare Has: \n{}".format(user_types),'\n')
    print('*'*10)

    if city != 'washington':

        # TO DO: Display counts of gender
        users_gender = df['Gender'].value_counts()
        print("The Count of Genders: \n{}".format(users_gender), '\n')
        print('*'*10)

        # TO DO: Display earliest, most recent, and most common year of birth
        earlyiest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])

        print("The earliest year of birth is: {} ".format(earlyiest_year), '\n')
        print("The most recent year of birth is: {} ".format(recent_year), '\n')
        print("The most common year of birth is: {} ".format(common_year), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------

def raw_data(df):
    row = 0
    while True:
        answer = input('\nWould you like to see some raw data? Please enter yes or no: ').lower()
        if answer not in ['yes', 'no']:
            print(Fore.RED + '**Please enter a valid input, try again.**\n' + Style.RESET_ALL)
            continue
        elif answer == 'yes':
            print(df[row:row+5])
            row += 5
        else:
            break

#---------------------------------------------------------------------------------

def main():
    while True:
        city, month, day= get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        # asking user if he/she want to restart the program
        restart = input('\nWould you like to restart? Enter yes to continue, any other entry quits the program: \n')
        if restart.lower() != 'yes':
            print('Thank you')
            break


if __name__ == "__main__":
	main()
