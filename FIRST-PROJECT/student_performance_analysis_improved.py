import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up matplotlib style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Load the CSV file
print("Loading Student Performance Data...")
df = pd.read_csv('StudentsPerformance.csv')

# Display basic information about the dataset
print("\n=== BASIC DATASET INFORMATION ===")
print(f"Dataset shape: {df.shape}")
print(f"Number of students: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== BASIC STATISTICS ===")
print(df.describe())

# Clean column names for easier access
df.columns = df.columns.str.replace('/', '_').str.replace(' ', '_')

# Calculate average scores for each subject
print("\n=== AVERAGE SCORES BY SUBJECT ===")
math_avg = df['math_score'].mean()
reading_avg = df['reading_score'].mean()
writing_avg = df['writing_score'].mean()

print(f"Average Math Score: {math_avg:.2f}")
print(f"Average Reading Score: {reading_avg:.2f}")
print(f"Average Writing Score: {writing_avg:.2f}")

# Calculate total score and average
df['total_score'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['average_score'] = df['total_score'] / 3

print(f"Overall Average Score: {df['average_score'].mean():.2f}")

# VISUALIZATION 1: Subject Performance and Correlations
plt.figure(figsize=(16, 12))

# 1. Bar Chart - Average Scores by Subject
plt.subplot(2, 2, 1)
subjects = ['Math', 'Reading', 'Writing']
averages = [math_avg, reading_avg, writing_avg]
bars = plt.bar(subjects, averages, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.title('Average Scores by Subject', fontsize=14, fontweight='bold')
plt.ylabel('Average Score')
plt.ylim(0, 100)
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{averages[i]:.1f}', ha='center', va='bottom', fontweight='bold')

# 2. Scatter Plot - Math vs Reading Scores
plt.subplot(2, 2, 2)
plt.scatter(df['math_score'], df['reading_score'], alpha=0.7, color='#FF1493', s=30, edgecolors='black', linewidth=0.5)
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.title('Math vs Reading Scores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Add correlation coefficient
correlation = df['math_score'].corr(df['reading_score'])
plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
         transform=plt.gca().transAxes, bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))

# 3. Scatter Plot - Reading vs Writing Scores
plt.subplot(2, 2, 3)
plt.scatter(df['reading_score'], df['writing_score'], alpha=0.7, color='#8B4513', s=30, edgecolors='black', linewidth=0.5)
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title('Reading vs Writing Scores', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Add correlation coefficient
correlation_rw = df['reading_score'].corr(df['writing_score'])
plt.text(0.05, 0.95, f'Correlation: {correlation_rw:.3f}', 
         transform=plt.gca().transAxes, bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))

# 4. Heatmap - Correlation Matrix
plt.subplot(2, 2, 4)
numeric_columns = ['math_score', 'reading_score', 'writing_score', 'total_score']
correlation_matrix = df[numeric_columns].corr()

# Create custom labels for better readability
custom_labels = ['Math\nScore', 'Reading\nScore', 'Writing\nScore', 'Total\nScore']
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.3f', cbar_kws={'shrink': 0.8},
            xticklabels=custom_labels, yticklabels=custom_labels)
plt.title('Score Correlation Heatmap', fontsize=14, fontweight='bold')
# Improve axis labels
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Subjects', fontsize=12)
plt.xticks(rotation=0, ha='center')
plt.yticks(rotation=0)

plt.tight_layout(pad=4.0, w_pad=3.0, h_pad=3.0)
plt.show()

# VISUALIZATION 2: Demographic Analysis
plt.figure(figsize=(15, 10))

# 1. Bar Chart - Average Scores by Gender
plt.subplot(2, 2, 1)
gender_scores = df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()
x = np.arange(len(gender_scores.index))
width = 0.25

plt.bar(x - width, gender_scores['math_score'], width, label='Math', color='#FF6B6B')
plt.bar(x, gender_scores['reading_score'], width, label='Reading', color='#4ECDC4')
plt.bar(x + width, gender_scores['writing_score'], width, label='Writing', color='#45B7D1')

plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.title('Average Scores by Gender', fontsize=14, fontweight='bold')
plt.xticks(x, gender_scores.index)
plt.legend()

# 2. Bar Chart - Average Scores by Parental Education
plt.subplot(2, 2, 2)
education_scores = df.groupby('parental_level_of_education')['average_score'].mean().sort_values(ascending=False)
plt.bar(range(len(education_scores)), education_scores.values, color='#96CEB4')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
plt.title('Average Scores by Parental Education', fontsize=14, fontweight='bold')
plt.xticks(range(len(education_scores)), 
           [label.replace(' ', '\n') for label in education_scores.index], 
           rotation=0, ha='center')

# 3. Heatmap - Average Scores by Gender and Race/Ethnicity
plt.subplot(2, 2, 3)
pivot_table = df.pivot_table(values='average_score', index='gender', columns='race_ethnicity', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='YlOrRd', fmt='.1f', cbar_kws={'shrink': 0.8})
plt.title('Average Scores by Gender and Race/Ethnicity', fontsize=14, fontweight='bold')

# 4. Performance comparison across different factors
plt.subplot(2, 2, 4)
factors = ['gender', 'lunch', 'test_preparation_course']
factor_labels = ['Gender', 'Lunch Type', 'Test Prep']
factor_effects = []
for factor in factors:
    factor_scores = df.groupby(factor)['average_score'].mean()
    effect = factor_scores.max() - factor_scores.min()
    factor_effects.append(effect)

plt.bar(factor_labels, factor_effects, color=['#FF7675', '#74B9FF', '#00B894'])
plt.xlabel('Factors')
plt.ylabel('Score Difference (Max - Min)')
plt.title('Impact of Different Factors on Performance', fontsize=14, fontweight='bold')

plt.tight_layout(pad=3.0)
plt.show()

# VISUALIZATION 3: Distribution Analysis
plt.figure(figsize=(15, 10))

# 1. Distribution of Total Scores
plt.subplot(2, 2, 1)
plt.hist(df['total_score'], bins=30, color='#74B9FF', alpha=0.7, edgecolor='black')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.title('Distribution of Total Scores', fontsize=14, fontweight='bold')
plt.axvline(df['total_score'].mean(), color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {df["total_score"].mean():.1f}')
plt.legend()

# 2. Box Plot - Scores by Test Preparation
plt.subplot(2, 2, 2)
df_melted = df.melt(id_vars=['test_preparation_course'], 
                    value_vars=['math_score', 'reading_score', 'writing_score'],
                    var_name='subject', value_name='score')
sns.boxplot(data=df_melted, x='test_preparation_course', y='score', hue='subject')
plt.title('Score Distribution by Test Preparation', fontsize=14, fontweight='bold')
plt.xlabel('Test Preparation Course')
plt.ylabel('Score')

# 3. Bar Chart - Average Scores by Lunch Type
plt.subplot(2, 2, 3)
lunch_scores = df.groupby('lunch')[['math_score', 'reading_score', 'writing_score']].mean()
x = np.arange(len(lunch_scores.index))
width = 0.25

plt.bar(x - width, lunch_scores['math_score'], width, label='Math', color='#FF6B6B')
plt.bar(x, lunch_scores['reading_score'], width, label='Reading', color='#4ECDC4')
plt.bar(x + width, lunch_scores['writing_score'], width, label='Writing', color='#45B7D1')

plt.xlabel('Lunch Type')
plt.ylabel('Average Score')
plt.title('Average Scores by Lunch Type', fontsize=14, fontweight='bold')
plt.xticks(x, lunch_scores.index)
plt.legend()

# 4. Bar Chart - Average Scores by Race/Ethnicity
plt.subplot(2, 2, 4)
race_scores = df.groupby('race_ethnicity')['average_score'].mean().sort_values(ascending=False)
plt.bar(range(len(race_scores)), race_scores.values, color='#DDA0DD')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Average Score')
plt.title('Average Scores by Race/Ethnicity', fontsize=14, fontweight='bold')
plt.xticks(range(len(race_scores)), race_scores.index, rotation=45, ha='right')

plt.tight_layout(pad=3.0)
plt.show()

# Additional Analysis - Performance by Test Preparation
print("\n=== PERFORMANCE BY TEST PREPARATION ===")
test_prep_analysis = df.groupby('test_preparation_course')[['math_score', 'reading_score', 'writing_score', 'average_score']].mean()
print(test_prep_analysis)

# Performance by Lunch Type
print("\n=== PERFORMANCE BY LUNCH TYPE ===")
lunch_analysis = df.groupby('lunch')[['math_score', 'reading_score', 'writing_score', 'average_score']].mean()
print(lunch_analysis)

# Performance by Race/Ethnicity
print("\n=== PERFORMANCE BY RACE/ETHNICITY ===")
race_analysis = df.groupby('race_ethnicity')[['math_score', 'reading_score', 'writing_score', 'average_score']].mean()
print(race_analysis)

# Summary Statistics and Insights
print("\n=== KEY INSIGHTS AND OBSERVATIONS ===")
print("\n1. SUBJECT PERFORMANCE:")
print(f"   - Reading has the highest average score ({reading_avg:.2f})")
print(f"   - Writing is second ({writing_avg:.2f})")
print(f"   - Math has the lowest average score ({math_avg:.2f})")

print(f"\n2. SCORE CORRELATIONS:")
print(f"   - Math and Reading correlation: {correlation:.3f}")
print(f"   - Reading and Writing correlation: {correlation_rw:.3f}")
print(f"   - Math and Writing correlation: {df['math_score'].corr(df['writing_score']):.3f}")

print(f"\n3. GENDER DIFFERENCES:")
gender_diff = df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()
print(f"   - Math: {'Females' if gender_diff.loc['female', 'math_score'] > gender_diff.loc['male', 'math_score'] else 'Males'} perform better")
print(f"   - Reading: {'Females' if gender_diff.loc['female', 'reading_score'] > gender_diff.loc['male', 'reading_score'] else 'Males'} perform better")
print(f"   - Writing: {'Females' if gender_diff.loc['female', 'writing_score'] > gender_diff.loc['male', 'writing_score'] else 'Males'} perform better")

print(f"\n4. TEST PREPARATION IMPACT:")
prep_impact = df.groupby('test_preparation_course')['average_score'].mean()
if len(prep_impact) > 1:
    print(f"   - Students with test preparation: {prep_impact.get('completed', 0):.2f}")
    print(f"   - Students without test preparation: {prep_impact.get('none', 0):.2f}")
    print(f"   - Improvement: {prep_impact.get('completed', 0) - prep_impact.get('none', 0):.2f} points")

print(f"\n5. SOCIOECONOMIC FACTORS:")
lunch_impact = df.groupby('lunch')['average_score'].mean()
if len(lunch_impact) > 1:
    print(f"   - Standard lunch students: {lunch_impact.get('standard', 0):.2f}")
    print(f"   - Free/reduced lunch students: {lunch_impact.get('free/reduced', 0):.2f}")
    print(f"   - Gap: {lunch_impact.get('standard', 0) - lunch_impact.get('free/reduced', 0):.2f} points")

print(f"\n6. PARENTAL EDUCATION IMPACT:")
print(f"   - Highest performing group: {education_scores.index[0]} ({education_scores.iloc[0]:.2f})")
print(f"   - Lowest performing group: {education_scores.index[-1]} ({education_scores.iloc[-1]:.2f})")
print(f"   - Education gap: {education_scores.iloc[0] - education_scores.iloc[-1]:.2f} points")

print(f"\n7. OVERALL STATISTICS:")
print(f"   - Total students analyzed: {len(df)}")
print(f"   - Overall average score: {df['average_score'].mean():.2f}")
print(f"   - Standard deviation: {df['average_score'].std():.2f}")
print(f"   - Highest total score: {df['total_score'].max()}")
print(f"   - Lowest total score: {df['total_score'].min()}")
