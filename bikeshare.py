# -*- coding: utf-8 -*-
"""
Created on Tue May 19 02:46:47 2020

@author: 96655
"""


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
    while True:
        city = input("\n What city would you like to choose? chicago , new york city, washington. \n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("invalid input, try one more time with a valid city")
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n which months would you prefer? january, februray, march, april, june or type all for all months.\n").lower()
        if month in ('january', 'februray', 'march', 'april', 'june', 'all'):
            break
        else:
            print("invalid input, try with a valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n what day would choose? sunday, monday,tuesday,wednesday, thursday, friday,saturday or type all for all days .\n").lower()
        if day not in('sunday', 'monday','tuesday','wednesday','thursady','friday','saturday', 'all'):
            print('invalid input, try one more time with a valid day')
            continue
        else:
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
    df= pd.read_csv(CITY_DATA[city])
   
    # convert start time to date time     
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    #extract month and day from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
    #filter by month
    if month != 'all':
        #using the month index to get the exact int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #flitering by month to have a dataframe
        df = df[df['month'] == month]
       
        #filtering day by week 
    if day !='all':
        df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("most common month:", common_month)


    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("most common day:", common_day)


    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("most common start hour:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print( "common used start station:",start_station) 


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print( "\n common used end station:", end_station)
    


    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('\n most common used combination of start and end station trip:', start_station, " and ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time converting seconds to days
    total_travel = df['Trip Duration'].sum()
    print("total travel time:",total_travel/86400 , "days")


    # TO DO: display mean travel time converting seconds to minutes
    mean_travel = df["Trip Duration"].mean()
    print("mean travel time:", mean_travel/60, "minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Types:\n", user_types)


    # TO DO: Display counts of gender
    try:
        gender_types = df["Gender"].value_counts()
        print("\n Gender Types:\n", gender_types)
    except KeyError:
        print("\n Gender Types:\n no data available")
    # except keyerror is used to handel washington which has no gender_types 

    # TO DO: Display earliest, most recent, and most common year of birth
    
    #most earliest birth year
    try:
        earliest_birth = df["Birth Year"].min()
        print("\n earliest birth:", earliest_birth)
    except KeyError:
        print("\n earliest birth: \n no data for this month.")
    #most recent birth year
    try:
        recent_birth = df["Birth Year"].max()
        print("\n recent birth:", recent_birth)
    except KeyError:
        print("\n recent birth: \n no data for this month.")
    #most common birth year
    try:
        common_birth = df["Birth Year"].value_counts().idxmax()
        print("\n common birth:",common_birth)
    except KeyError:
        print("\n common birth: \n no data for this month")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    while (True):
        X = input('\n choose (yes) to see row data or (no) for not.\n>')
        if ( X== "yes"): 
            print(df.iloc[i:i+5])
            i+=5
        elif (X == "no"):
            break
             
            
    return
        

#ask the user if want to see raw data . user choose yes will display 5 lines of row data and whenever click yes it will show again 5 more lines of row data, until the user choose no. 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
