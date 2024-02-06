# vanguard-ab-test
Project status - Active

# Project objective


# Methods

General
- Head
- Shape
- Info
- Dtypes

Cleaning 
- Drop na values
- Duplicated
- Nunique

Tranformation
- Merges
- Filtering
- Grouping (loc, mask)
- Sort values
  
Exploratory Data Analysis (EDA)
  - Value Counts
  - Info 
  - Describe (Mean, Median, Mode, Percentiles , Min, Max)  
  
# Technologies

- Python
- Pandas
- Seaborn
- Statsmodels.api
- Matplotlib.pyplot
- Numpy
- Scipy.stats
- Tableau 

# Project Description
An A/B test was set into motion from 3/15/2017 to 6/20/2017 by the team.

* **Control Group**: Clients interacted with Vanguard’s traditional online process.
* __Test Group__: Clients experienced the new, spruced-up digital interface.

Both groups navigated through an identical process sequence: an initial page, three subsequent steps, and finally, a confirmation page signaling process completion.

The goal is to see if the new design leads to a better user experience and higher process completion rates.

The experiment counted with 3 datasets:

1. Client Profiles (df_final_demo): Demographics like age, gender, and account details of our clients.
2. Digital Footprints (df_final_web_data): A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These two files were merged into one comprehensive data frame.
3. Experiment Roster (df_final_experiment_clients): A list revealing which clients were part of the grand experiment.


# Steps
During the project we found the need to create new datafames to better utilize the data that was gathered during the experiment. 

- df_online: We discovered that we had more client profiles than those within the experiment roster, so we created a dataframe with the clients that were part of the experiment and their demographic information. 

- df_ab: We wanted to be able to know the demographic information about the users that participated and their digital footprints, so we created this dataframe to analyze this information.

To properly understand the effects of the experiment, we had to filter the afformentioned dataframe (df_ab) into two dataframes:
- df_test = The filtered data of the clients from the Test Group.

- df_control: The filtered data of the clients from the Control Group.

  We chose to utilize 2 success metrics (KPI's) for our analysis,
  - Completion Rate
  - Time Spent on Each Step

  For our hypothesis testing, we tested for 3 hypothesis:
  - Completion Rate
  - Completion Rate with a Cost-Effectiveness Threshold (5%)
  - Difference on steps

To test for the Difference on steps, we need to know that the order of the process is: 
1. start
2. step 1
3. step 2
4. step 3
5. confirm

In order to test for the difference of time between the steps, we needed to create 2 new dataframes that have only the entries that have steps in sequential order,
df_control_time_each_step and df_test_time_each_step.

# Conclusion
After testing for the three hypothesis, we ended up with the following insights:
- Completion Rate: Reject the null hypothesis, there is a significant difference in completion rates between the test and control groups
- Completion Rate with a Cost-Effectiveness Threshold (5%): Reject the null hypothesis. The observed increase in completion rate is statistically significant but it does not meet the 5% threshold placed by the company.
-  Difference on steps: Fail to reject the null hypothesis. The means of the time per step are not significantly different.

  With this information, we can answer the question that was posed:
  *Would these changes encourage more clients to complete the process?*
  
The answer to that question would that although we rejected 2 of our null hypothesis (Completion Rate and Completion Rate with a Cost-Effectiveness Threshold (5%)), the Cost-Effectiveness Threshold did not reach the 5% established by the stakeholders so it did not fufill the goal we needed it to. Aditionally, we also failed to reject the null hypothesis for the Difference on steps. 

This leads us to say that although there is proof that the changes to the UI made the completion rate increase, because of the failure to meet the 5% threshold and the failure to see a difference in the average time spent on each process step, our conclusion is that the changes did encourage more clients to complete the process but not to the standards that were expected. 

To see the presentation of this project, you can access it with the following link: https://docs.google.com/presentation/d/1yzm5lO-8LBUAf2Z0ifebm9R5nRtfD0uuzLtm2PZHlsw/edit?usp=sharing
# Contact
- https://www.linkedin.com/in/axel-lopez-cabezas-213194170/
