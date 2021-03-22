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

    
    
    while True:
      city=input("\nWould you like to see data for Chicago, New York City or Washington?\n").lower()
      if city not in ('chicago','new york city','washington'):
          print ('The city out of the scope\n Please try again..')
          continue
      else:
          break
            
    while True:
           month= input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
           if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
              print("The month out of the scope\n Please try again..")
              continue
           else:
              break

    while True:
            day= input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
            if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
               print("The day out of the scope\n Please try again..")
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
          months = ['january', 'february', 'march', 'april', 'may', 'june']
          month = months.index(month) + 1
            
          df = df[df['month'] == month]

    if day != 'all':
          df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
# Return counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

# Return counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")


# Return earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
         view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
         start_loc = 0
         while (view_data == 'yes'):
              print(df.iloc[start_loc:start_loc+5])
              start_loc += 5
              view_display = input("Do you wish to continue?: ").lower()
              if (view_display!= 'yes'):
                 break
                    
     


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


   # By Atheer
