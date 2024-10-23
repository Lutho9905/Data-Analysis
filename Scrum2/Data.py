import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'data.csv'
data = pd.read_csv(file_path)

filtered_data = data[(data['averageRating'] > 7 ) & (data['releaseYear']>2010)]

# Create a new column 'ratingCategory' based on averageRating
def categorize_rating(rating):
    if rating >= 8:
        return 'Excellent'
    elif rating >= 6:
        return 'Good'
    else:
        return 'Average'

filtered_data['ratingCategory'] = filtered_data['averageRating'].apply(categorize_rating)

# Group by releaseYear and aggregate averageRating and numVotes
grouped_data = filtered_data.groupby('releaseYear').agg(
    averageRating=('averageRating', 'mean'),
    totalVotes=('numVotes', 'sum')
).reset_index()

# Find the year with the highest average rating
highest_rating_year = grouped_data.loc[grouped_data['averageRating'].idxmax()]
print("Year with highest average rating:", highest_rating_year)

# Set style for plots
sns.set(style="whitegrid")

# Figure setup for multiple plots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Histogram for averageRating
sns.histplot(data['averageRating'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Average Ratings')
axes[0, 0].set_ylabel('Movies')
axes[0, 0].set_xlabel('Average Rating')

# Histogram for numVotes (log scale for better readability)
sns.histplot(data['numVotes'], bins=20, kde=True, log_scale=(True, False), ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Number of Votes (Log Scale)')
axes[0, 1].set_xlabel('Number of Votes')

# Boxplot of averageRating by releaseYear
sns.boxplot(x='releaseYear', y='averageRating', data=data, ax=axes[1, 0])
axes[1, 0].set_title('Average Rating by Release Year')
axes[1, 0].tick_params(axis='x', rotation=90)

# Scatter plot of averageRating vs. numVotes
sns.scatterplot(x='numVotes', y='averageRating', data=data, ax=axes[1, 1])
axes[1, 1].set_title('Average Rating vs. Number of Votes')
axes[1, 1].set_xlabel('Number of Votes')
axes[1, 1].set_ylabel('Average Rating')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
