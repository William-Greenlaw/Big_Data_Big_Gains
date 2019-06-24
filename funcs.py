def calculate_age(x):
    '''
    Calculate how old I am on a particular date
    '''
    # source: https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python/2259711
    # My age is today's year minus the year of my birth.
    born = date(1995, 1, 1)
    age = x.year - born.year - ((x.month, x.day) < (born.month, born.day))
    return age

def Intensity():
    '''
    Produce workout intensity table.
    '''
    intensity = pd.DataFrame()

    intensity['response'] = ['strength', 'strength and hypertrophy', 'hypertrophy']

    # set 1rm max range and then reverse to fit the table
    intensity['intensity'] = pd.IntervalIndex.from_breaks([.6, .75, .85, 1], closed = 'left')[::-1]
    intensity['reps_per_set'] = pd.IntervalIndex.from_breaks([1,3,8,12], closed = 'both')
    intensity['low_volume'] = pd.IntervalIndex.from_breaks([1,5,15,25], closed = 'left')
    intensity['moderate_volume'] = pd.IntervalIndex.from_breaks([5, 15, 25, 50], closed = 'left')
    intensity['high_volume'] = pd.IntervalIndex.from_breaks([15, 25, 50, np.inf], closed = 'left')
    
    return intensity