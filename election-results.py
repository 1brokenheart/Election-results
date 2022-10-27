import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Mehmet Oz', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz','John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 
'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz',
'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'Mehmet Oz',
'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'Mehmet Oz', 'Mehmet Oz', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'John Fetterman', 'Mehmet Oz']

#total_votes = np.count_nonzero(survey_responses)
total_votes = len(survey_responses)
print('Number of people who voted  = ' + str(total_votes))

total_Mehmet_Oz = sum([1 for n in survey_responses if n == 'Mehmet Oz'])
print('Number of people who voted for Mehmet Oz = ' + str(total_Mehmet_Oz))

percentage_Mehmet_Oz = (total_Mehmet_Oz * 100) / total_votes
print('possibility that Mehmet Oz wins = ' + str(percentage_Mehmet_Oz) +' %')

possible_survey = np.random.binomial(70, 0.54, size=10000) / 70.

plt.hist(possible_survey, range=(0,1), bins=20)
plt.show()

Mehmet_Oz_loss_surveys = np.mean( possible_survey < 0.50)
print(Mehmet_Oz_loss_surveys)

large_survey = np.random.binomial(7000, 0.54, size=10000) / 7000.
plt.hist(large_survey, range=(0,1), bins=20)
plt.show()

Mehmet_Oz_loss_new = np.mean(large_survey < 0.50)
print('The probability that Mehmet Oz losses if the survey was for 7,000 people instead of 70 people = ' + str(Mehmet_Oz_loss_new))
