'''
No code should go in this file.


Rubric items should be brought into a seperate dataframe for it's own use.

So far from student answers the only information that needs to be brought into a dataframe in terms of feeding it into an agent is:
    -Attempt ID(Index)
    -Q Version
    -Student Answer
    -Answer Match
    
Also Answer match could instead be score where we take the Agent's graded points.

##########################################################################################################################################
Idea for sample templates being fed into the ai. General structure
    -First provide full question and context of the question
    -Second is give each individual rubric item alongside their description, scoring guide and points
    -Provide student answer as the answer to be evalulated.
    -Prompt AI agent to provide a numeric score for each of the rubric items and a reason for said scores
    -The Score and reason provided will be saved into CSV or some other format.
    -Maybe ask for a confidence in it's own score as well?
##########################################################################################################################################    
Prompt Enginering Course:
https://www.deeplearning.ai/courses/chatgpt-prompt-eng
https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/dfbds/introduction?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button

##########################################################################################################################################     
From observations of dataframes, repeating the same student answer text across each index will consume significantly more memory
than a second dataframe that contains the questions themselves and pairing them up when needed.

Idea A.)Have each question have a unique test ID and question ID to form a unique ID
Idea B.) Have each question just have a unique question ID

Question IDs would also allow the agent to access the provided question solution with greater ease than other solutions.
'''