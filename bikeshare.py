import time
import calendar
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
    global city, month, day
    city = " "
    month = " "
    day = " "
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see the data for Chicago, New York city or Washington?\n").lower()
    while city not in CITY_DATA:
            print("Oops it seems not right! Please enter the city name again.")
            city = input("Would you like to see the data for Chicago, New York city or Washington?\n").lower()

    # get use user choose the filter they want
    fil = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter\n").lower()
    while fil not in ['month', 'day', 'both', 'none']:
        print("Invaild entry, please try again:")
        fil = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter\n").lower()
<<<<<<< HEAD

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
||||||| merged common ancestors
    
    # TO DO: get user input for month (all, january, february, ... , june)   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
=======

    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
>>>>>>> refactoring
    while fil in ['month', 'day', 'both', 'none']:
        # User wants to be filtered by both month and day
        if fil == 'both':
            month = input("Which month would you like to fliter the data by, or not at all? January, February, March, April, May, or June?\n").lower()
            while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                print("Invaild entry, please try again:")
                month = input("Which month would you like to fliter the data by, or not at all? January, February, March, April, May, or June?\n").lower()
            day = int(input("Which day? Please enter an interger(0 = Monday, 1 = Tuesday...)\n"))
            while day not in [0, 1, 2, 3, 4, 5, 6]:
                print("Invaild entry, please try again:")
                day = int(input("Which day? Please enter an interger(0 = Monday, 1 = Tuesday...)\n"))
<<<<<<< HEAD

||||||| merged common ancestors
                      
=======
        #User wants to be filtered by month only
>>>>>>> refactoring
        elif fil == 'month':
            month = input("Which month would you like to fliter the data by, or not at all? January, February, March, April, May, or June?\n").lower()
            while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                print("Invaild entry, please try again:")
                month = input("Which month would you like to fliter the data by, or not at all? January, February, March, April, May, or June?\n").lower()
            day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
<<<<<<< HEAD

||||||| merged common ancestors
            
=======
        #User wants to be filtered by day only
>>>>>>> refactoring
        elif fil == 'day':
            month = ['january', 'february', 'march', 'april', 'may', 'june']
            day = int(input("Which day? Please enter an interger(0 = Monday, 1 = Tuesday...)\n"))
            while day not in [0, 1, 2, 3, 4, 5, 6]:
                print("Invaild entry, please try again:")
                day = int(input("Which day? Please enter an interger(0 = Monday, 1 = Tuesday...)\n"))

        else:
            month = ['january', 'february', 'march', 'april', 'may', 'june']
            day = [0, 1, 2, 3, 4, 5, 6]

        break


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
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("\nWhat's the most popular month to travel?\n")
    print(calendar.month_name[common_month])
    print("\nWhat's the most popular day to travel?\n")
    print(calendar.day_name[common_day])
    print("\nWhat's the most popular hour to travel?\n")
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_month, common_day, common_hour


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().index[0]

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().index[0]

    # display most frequent combination of start station and end station trip
    df['Comb Station'] = df['Start Station'] + ',' + df['End Station']
    common_comb_station = df['Comb Station'].value_counts().index[0]

    print("\nwhat's the most popular start station?\n")
    print(common_start_station)
    print("\nwhat's the most popular end station?\n")
    print(common_end_station)
    print("\nwhat's the most popular combination of start station and end station?\n")
    print(common_comb_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_start_station, common_end_station, common_comb_station


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("\nwhat's the total travl time?\n")
    print(total_travel_time)
    print("\nwhat's the average travl time?\n")
    print(mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return total_travel_time, mean_travel_time

def user_stats(df):
    """Displays statistics on bikeshare users."""
    global gender, early_year, recent_year, common_year
    gender = " "
    early_year = 0
    recent_year = 0
    common_year = 0

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("\nWhat's the breakdown of users?\n")
    print(user_type)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nWhat's the breakdown of gender\n")
        print(gender)
        pass
    except KeyError:
        print("\nThere is no gender information.\n")
        pass

    # Display earliest, most recent, and most common year of birth
    try:
        early_year = df.sort_values(by = 'Birth Year', ascending = True, na_position = 'last').head(n=1)
        recent_year = df.sort_values('Birth Year', ascending = False, na_position = 'last').head(n=1)
        common_year = df['Birth Year'].mode()
        print("\nWhat's the oldest, youngest, and most popular year of birth, respectively?\n")
        print(early_year, recent_year, common_year)
        pass
    except KeyError:
        print("\nThere is no birth year information.\n")
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return user_type, gender, early_year, recent_year, common_year

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input("\nWould you like to see some raw data? yes or no.\n").lower()
        while raw_data not in ['yes', 'no']:
            print("\nI don't get it...\n")
            raw_data = input("\nWould you like to see some raw data? yes or no.\n").lower()

        if raw_data == 'yes':
            print(df.iloc[0:5])
        else:
            print("uhmmmm.....")
<<<<<<< HEAD
||||||| merged common ancestors
        
=======

>>>>>>> refactoring

        # Ask if the user would like to see more result
        i = 0
        j = 0
        for j in range(df.shape[0]):
            more_data = input("\nWould you like to see more data?\n").lower()
            i = i + 5
            while i < df.shape[0]:
                if more_data == 'yes':
                    print(df.iloc[i:i+5])
                    break
                elif more_data == 'no':
                    break
            else:
                continue
            break
        else:
            continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
