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
    city = str(input("Please enter the name of the city (chicago, new york city or washington):" ).lower())
    while city not in ('chicago', 'new york city', 'washington') :
            city = str(input('Please enter a valid city (chicago, new york city or washington):' ).lower())
    # TO DO: get user input for month (all, january, february, ... , june)
    month = (input("Which month you'd like to explore (all, january, february, ... , june):" ).lower())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = (input("Which day of the week you'd like to explore (all, monday, tuesday, ... sunday):" ).lower())

    #not in command is learned from Stackoverflow , https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
    #Input command is learned in the UDACITY lectures.
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_in_a_week'] = (df['Start Time'].dt.weekday_name)

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_in_a_week'] == day.title()]

    #.read_csv and .title() methods are learned in the UDACITY lectures.
    #Other pandas methods are obtained from https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    month = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[month - 1].capitalize()

    # TO DO: display the most common day of week
    common_day = df['day_in_a_week'].value_counts().reset_index()['index'][0]


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df.hour.mode()[0]


    print ("The most common month : %s " % common_month)
    print ("The most common day : %s " % common_day)
    print ("The most common start hour : %s " % common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #.capitalize and .value_counts() methods are obtained from UDACITY lectures.
    #.reset_index () method is obtained from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
    #Other pandas methods are obtained from https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().reset_index()['index'][0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().reset_index()['index'][0]

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_startend = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)

    print(" The most commonly used start station : %s " % common_start_station)
    print(" The most commonly used end station : %s " % common_end_station)
    print(" The most frequent combination of start and end station trip : %s " % combination_of_startend)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #.groupby and size methods are from UDACITY lectures.
    #.nlargest method is obtained from https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.nlargest.html

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("Total travel time : %s seconds" % total_travel_time)
    print("Mean travel time : %s seconds" % mean_travel_time)
    print('-'*40)

    #.sum and .mean methods are from the lectures about NumPy

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if city != 'washington' :
        user_gender = df['Gender'] .value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(np.min(df['Birth Year']))
        recent = int(np.max(df['Birth Year']))
        common_birth = int(df['Birth Year'].mode()[0])
        print("Number of user gender : %s" % user_gender)
        print("The earliest year of birth : %s" % earliest)
        print("The most recent year of birth : %s" % recent)
        print("The most common year of birth : %s" %common_birth)
    else:
        print( "There is no data about user's gender and birth for Washington." )


    print("Number of user types : %s" % user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #.min, .max and .mode methods are from the lectures about NumPy

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        rawdata = input('Would you like to see the first five lines of the raw data?')
        if rawdata.lower() != 'yes':
            break
        else:
            print( df.head() )  #.head() is from our Pandas DataFrame lecture.
            row_number = 5
            more_raw = input('Would you like to see five more lines of the raw data?')
            while more_raw.lower() == 'yes':
                row_number += 5
                print( df.head(row_number) )
                more_raw = input('Would you like to see five more lines of the raw data?')


        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
