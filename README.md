# Big Data, Big Gains

## Relational Database Structure:  The Gains Database
- Routines
    - Routines should consist of exercises, a routine name, and a prescribed number of sets and reps for a progression strategy
    - Each exercise for a given time period should belong to only one routine with no overlap
- Workouts
- Exercises
- Sets
- Separate cardio table?
- Intensities
- 1 Rep Max

## Data Collection Protocol
### Weight


### Fitbit Biometrics
- Fitbit data includes the following:
    - Calories burned
    - Steps taken
    - Floors climbed
    - Heart rate
    - Distance traveled
    - Current elevation
- Fitbit data is collected using a Fitbit Charge HR device. 
    - From 2014 to 2016, Fitbit Charge HR
    - From 2016 to 2018, Fitbit Charge HR2
    - From 2018 to present, Fitbit Charge HR3
- The wrist the device is worn on alternates from time to time to give my wrist a rest, but more often than not, my left wrist is the Fitbit wrist.
- The Fitbit device is worn with the face of the device on the inside of my wrist.
- At the beginning of each workout, starting with the warmup, I activate the Fitbit activity monitor.
- At the end of each workout, after cooldown if a cooldown was done, I deactivate the Fitbit activity monitor.
    - Occassionally, I will forget to start or stop the tracker promptly, resulting in some error.
- The activity monitor used is one of the following:
    - Sport when "sport" was all that was available.
    - Weights when "weights" was introduced to the Fitbit device.
- Heart rate data is then pulled from my Fitbit account using the API.

### Workouts
#### Lifting
- Workouts are recorded using the Fitnotes Android application.
- All workout days represent a single, continuous workout session since I don't work out more than once a day 
- As of May 18th, 2018, workouts are done exclusively as parts of defined routines:
    - All exercises and all sets in a routine are slotted for a workout day's entry, even if they are not completed in the gym in order to track completion rate.
    - If an exercise or set is not completed, its weight or distance is set to 0 to indicate it was not done.
- For now, whether or not I did a cooldown/stretch at the end of the workout is recorded but not necessarily what kind of stretches or cooldown work
    - Cooldown stretch data is also largely missing before 2017, so that data is incomplete
#### Cardio
- I have done a poor job of tracking cardio generally, so the data on cardio is incomplete. Martial Arts Tabatas for example have not been categorized as cardio.


## Limits
- Muscle group labels are only an appromixation of which muscle does most of the work on a particular kind of exercise. Really, multiple muscle groups across the body work together during a workout, so saying an exercise is a "chest" exercise somewhat overshadows the role that the shoulders and triceps play during a benchpress. In the future, it could be wise to have an exercise database that ranks what proportion of the exercise a muscle group contributes to.


