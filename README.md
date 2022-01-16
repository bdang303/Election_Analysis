# Election Analysis using Python

## Overview of Election Analysis
A dataset of votes from a U.S. Congressional election in Colorado was provided that contained ballots for candidate votes in multiple counties. Using a python script to conduct an automated analysis, we were able to store the data elements from a CSV file using lists & dictionaries. The script allowed us to access the data and perform various calculations to determine the results of the election. In addition to the results, the script also summarized and reported out details via a text file.

## Election Audit Results
•	How many votes were cast in this congressional election? In this election, there were a total of 369,711 votes cast
•	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. There were 3 Counties where votes were tabulated, Denver had the majority of votes at 306,055 (82.8%), following by Jefferson County with 38,855 votes (10.5%), and Arapahoe County with 24,801 (6.7%). To calculate the number of votes, a “For” loop was created to retrieve the county votes for each county:

    for county_name in county_votes:
        cvotes = county_votes.get(county_name)

Using the following formula, we calculated the percentage of results:

        countyvote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {countyvote_percentage:.1f}% ({cvotes:,})\n")


•	Which county had the largest number of votes? Per the breakdown above, Denver had the largest County turnout in this election. 
•	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 3 Candidates were in the running in this election. Diana DeGette had 272,892 votes, followed by Charles Casper Stockham with 85,213 votes, and Raymon Anthony Doane with 11,606 votes.
•	Which candidate won the election, what was their vote count, and what was their percentage of the total votes? Diana DeGette was the candidate who received the most votes with 272,892 votes which was 73.8% of the total votes and therefore the winner of the election.

![Election Summary]( https://github.com/bdang303/Election_Analysis/blob/main/Resources/Election_Summary.png)


## Election Audit Summary
The python script that was created to automate the election audit and results could definitely be utilized by the election commission for other elections. Not only can the base of this script be used for county elections, it can be modified to be used for local elections at the city level (ex. Mayor Elections). To do so, we can create separate lists & dictionaries to do this. In addition, if there were other positions or seats within an election, and that data was available via a separate column in the CSV file, we can modify the scrip to report out the winner of each position or seat. 
![image](https://user-images.githubusercontent.com/93288351/149644615-f21d6de6-83eb-4ade-b67e-6e51ab200de9.png)
