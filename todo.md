# Todo
## Database Work
[x] Create a separate table with a list of exercise features like equipment, push/pull, etc.
[] Categorize volume by rep ranges and intensities for strength and hypertrophy.
[] Finish classifying variants in exercise table.
[] Add sub-variants to exercise table, like horizontal push, horizontal pull
[] Revisit how to do body measurements to track progress
[] Revisit how to quantify ab work when comparing bodyweight to weighted exercises
[] Flatten Fitbit intraday data into separate tables.
[] Resolve the pull-up, chin-up definition problem.
[x] Merge together duplicate exercise names
    - I.E. Decline Cable Fly -> Low Cable Cross-Over
    - Decline Pull Up -> Inverted Row
[] Merge duration, start, and end time of workout into workout meta-data.
[] Fix primary lift and category issue that doesn't label when only cardio has been done.
[] Figure out how to model programming decisions.
[] Address weaknesses of rolling one rep max calculation.
[x] Add my estimated bodyweight to all variations of dips and pull-ups
[x] Integrate estimated bodyweight into one_rep_max table
[x] Record how many light, moderate, and heavy repetitions based on relative intensity; "relative volume"
[x] Track the intensity of each set; I.E. % of 1RM, 60%, 75%, 85% etc.
    - This would require calculating 1RMs at the beginning of the workout routine.
[x] Calculate relative volumes
[x] Integrate RPE into training data capture.
[x] Convert cardio distances to miles and miles per hour

## Macro Issues
[] Migrate project and jupyter computing environments into the cloud
[] Research and select a workflow/pipeline management system
[] Design jupyter books to hold each analysis

## Analyses
[] Sleep analysis
[] Total time resting vs. total time working out
[] % of time in heart rate zones

## Tools
[x] Write golden ratio range axis function for line charts that don't go to zero
[] Adjust golden ratio function to account for situations where the y-axis does not start at zero but
at the very least appears to do so.

## Research
[x] Read through one rep max literature
[] Research difference between primary, assistance, and auxiliary lifts
[] Proper warmup load strategy
    - Dynamic stretching warmup and post-workout cooldown specific to the day in the routine.
[] Load progression strategy
[] Cardio/work capacity strategy
[] 1 rep max selection and routine selection strategy
[x] Design a routine with multiple days per body part to split up the volume