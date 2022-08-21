import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Getting user input for city (chicago, new york city, washington). Using a while loop to handle invalid inputs
    while True:
        city = input('Which city are interested in : Chicago, New york city or Washington:\n').title()
        if city in ['Chicago', 'New York City' , 'Washington']:
            break
        print('Invalid entry, kindly try again')

    #  Getting user input for month (all, january, february, ... , june). Using a while loop to handle invalid inputs
    while True:
        month = input('US bikeshare data is available from January to June, please enter a specific month or all for all months:\n')
        if month.title() in ['January', 'February', 'March', 'April', 'May', 'June','All']:
            break
        print('Invalid entry, kindly try again')

    #  Getting user input for day of week (all, monday, tuesday, ... sunday). Using a while loop to handle invalid inputs
    while True:
        day = input('please enter a specific day to explore data or all for all days:\n')
        if day.title() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','All']:
            break
        print('Invalid entry, kindly try again')

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
    # Defining a dictionary as a reference for the city file
    CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
    # Reading the file to -df- data frame
    df = pd.read_csv(CITY_DATA[city])
    # Converting -Start Time- column to date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Create -month- column
    df['month'] = df['Start Time'].dt.month
    # Create -day- column
    df['day'] = df['Start Time'].dt.day_name()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # Filtering -df- by month if requested by the user
    if month != 'all':
        m_ind = months.index(month)+1
        df = df[(df.month == m_ind) ]
    # Filtering -df- by day if requested by the user
    if day != 'all':
        df = df[ df.day == day.title() ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculate and print the most common month
    common_month = df['month'].mode()[0]
    print ('The most common month of travel is: {} . *This stat. is accurate only if you choosed all months '.format (common_month))
    # Calculate and print the most common day of week
    common_day = df['day'].mode()[0]
    print ('The most common day of travel is: {} . *This stat. is accurate only if you choosed all days '.format (common_day))

    # Calculate and print the most common start hour
    common_s_hour = df['Start Time'].dt.hour.mode()[0]
    print ('The most common start hour of travel is: {} . *This stat. is accurate only if you choosed all months & all days'.format(common_s_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculate & print most commonly used start station
    common_s_station = df['Start Station'].mode()[0]
    print ('The most popular start station is: {} . *This info. is accurate only if you choosed all months & all days '.format (common_s_station))

    # Calculate & print most commonly used end station
    common_e_station = df['End Station'].mode()[0]
    print ('The most popular end station is: {} . *This info. is accurate only if you choosed all months & all days '.format (common_e_station))

    # Calculate & print most frequent combination of start station and end station trip
    station_combination= df['Start Station']+df['End Station']
    print('The most frequent combination of start station and end station trip is: {} . *This info. is accurate only if you choosed all months & all days '.format (station_combination.mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate & display total travel time
    print('Total travel time in seconds according to your selection is: ',df['Trip Duration'].sum())

    # Calculate & display mean travel time
    print('Average travel time in seconds per trip according to your selection is: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate & Display counts of user types
    print('The count of each user type is: \n\n', df.groupby(['User Type'])['User Type'].count())

    # Calculate & Display counts of gender if the user selected city is not Washington
    # Calculate & Display earliest, most recent, and most common year of birth if the user selected city is not Washington
    if city.title() != 'Washington':
        print('The count of each user gender is: \n\n', df.groupby(['Gender'])['Gender'].count())
        print('The oldest user of Bikeshare bikes was born in : {} \nThe youngest user of Bikeshare bikes was born in : {} \nThe most common birth year of Bikeshare users is : {}'.format(int(df['Birth Year'].min()),int(df['Birth Year'].max()),int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_dataframe(df):
    """Displays dataframe """
    # Asking user if he wants to view raw data & validate his answer
    while True:
        choice = input('Do you like to view the detailed data accoding to your selection y/n: \n')
        if choice.title() in ['Y','N']:
            break
        print('Invalid entry, kindly try again')
    # Define indecis if the answer is yes
    if choice.title() == 'Y':
        ind1 = 0
        ind2 = 4
        # Looping data 5 records for each yes entry
        while True:
            data_slice = df.ix[ind1:ind2]
            print(data_slice)
            while True:
                choice = input('next? y/n: \n')
                if choice.title() in ['Y','N']:
                    break
                print('Invalid entry, kindly try again')
            if choice.title() == 'N':
                break
            ind1 = ind1+5
            ind2 = ind2+5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_dataframe(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
