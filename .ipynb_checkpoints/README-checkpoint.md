# Big Data, Big Gains

## Relational Database Structure:  The Gains Database
- **Routines**
    - Routines should consist of exercises, a routine name, and a prescribed number of sets and reps for a progression strategy
    - Each (routine, exercise, split) should be unique. 
- **Exercises**
- **Sets**
    - Description: 
        - The sets table consists of each workout set of exercise repetitions performed during a workout. Given that a "set" is an arbitrary grouping of repetitions, to better delineate a set, sets generally adhere to the following rules:
            - Sets consist of multiple, continuous repetitions back-to-back followed by a period of rest.
            - If repetitions cease for more than five seconds, the set is over.
    - Columns:
        - Date: The date the set was completed.
        - Routine: The workout routine imported from the routines table. This is duplicative but makes analysis simple
        - Category: The primary muscle group affected by the exercise.
        - Exercise: The exercise performed during the set, I.E. "Flat Barbell Bench Press". Exercises should indicate in their titles...
            - Angle of the plane of motion, I.E. "Flat", "Incline", "Decline"
            - Equipment used, I.E. "Barbell", "Dumbbell", "Cable"
            - Name of the motion, I.E. "Bench Press", "Flys"
        - Weight: The amount of weight lifted during a given set.
        - One Rep Max: The largest Epley-formulated one repetition maximum within the last 30 *days*, not 30 *workouts*.
        - Intensity: The percentage of *One Rep Max* the *Weight* lifted was.
        - Volume: *Weight* times *Reps*.
        - Relative Volume: *Weight* times *Reps* times *Intensity*.
        - Distance Unit: The unit of distance used on cardio workouts, I.E. miles, meters.
        - Time: Time spent doing the exercise set, mainly for cardio workouts.
        - Comment: Any comments made manually on a set, sometimes to take not on how the set feels, to add supporting information to the way the set was performed, or to make note of the RPE, etc.
    - Limits:
        - While the data collection *within* a workout is generally very good, around 95% complete, there are some forms of exercise that may be missing:
        - Ab workouts difficult to record
            - I used to use an Android app to guide ab workouts but failed to record the sessions in Fitnotes properly. Instead, on days with ab work, Fitnotes comments read "Abs" but nothing further. Upon revisiting the app to try to recover the data, I discovered my progress seems to have been erased. As a result, I label inside the Fitnotes app any ab day without specifications as "Unspecified Ab Workout".
        - Stretches were not specifically recorded until 5-28-2019. 
            - Before then, streches were encoded only generally as "Active Stretching" or "Cooldown and Stretch". As of that date, stretches are logged as their own exercises with repetitions and time used instead of repetitions and weight. Active stretching done before a workout is spottily recorded at best and "Cooldown and Stretch" was only seriously maintained beginning in October 2016.
        - Exercises done outside of a workout are generally not recorded, I.E. if I played a game of pickup basketball with friends. While work is being done to expand to fitness generally, the gains database for now if geared toward strength training.

- Separate cardio table?

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
    - Weights when "weights" was introduced to the Fitbit device, even if only cardio is being done. There may be some error unaccounted for by doing so, but after manually testing my own heart rate compared to Fitbit's during cycling, the Fitbit generally assesses my heart rate satisfactorily. This simplifies export of Fitbit data to cross-reference with the Sets table.
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

### Limits
- Muscle group labels are only an appromixation of which muscle does most of the work on a particular kind of exercise. Really, multiple muscle groups across the body work together during a workout, so saying an exercise is a "chest" exercise somewhat overshadows the role that the shoulders and triceps play during a benchpress. In the future, it could be wise to have an exercise database that ranks what proportion of the exercise a muscle group contributes to.