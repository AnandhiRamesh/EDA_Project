import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Student Performance EDA Dashboard")

# Load dataset
# Load dataset
df = pd.read_csv("StudentsPerformance.csv")
# Dataset Preview
st.header("Dataset Preview")
st.dataframe(df.head())

# Dataset Shape
st.header("Dataset Information")
st.write("Number of Rows:", df.shape[0])
st.write("Number of Columns:", df.shape[1])

# Statistics
st.header("Statistical Summary")
st.write(df.describe())

# Missing Values
st.header("Missing Values")
st.write(df.isnull().sum())

# Column names
st.header("Columns in Dataset")
st.write(df.columns)

# Gender Analysis
st.header("Gender Distribution")

gender_count = df["gender"].value_counts()

fig, ax = plt.subplots()
ax.bar(gender_count.index, gender_count.values)
ax.set_xlabel("Gender")
ax.set_ylabel("Number of Students")
ax.set_title("Students by Gender")

st.pyplot(fig)


# Average Scores
st.header("Average Scores")

math_avg = df["math score"].mean()
reading_avg = df["reading score"].mean()
writing_avg = df["writing score"].mean()

st.write("Average Math Score:", round(math_avg,2))
st.write("Average Reading Score:", round(reading_avg,2))
st.write("Average Writing Score:", round(writing_avg,2))


# Score Distribution
st.header("Score Distribution")

score_column = st.selectbox(
    "Select Score Column",
    ["math score", "reading score", "writing score"]
)

fig, ax = plt.subplots()
ax.hist(df[score_column])
ax.set_xlabel(score_column)
ax.set_ylabel("Students")
ax.set_title("Score Distribution")

st.pyplot(fig)


# Correlation Heatmap
st.header("Correlation Between Scores")

fig, ax = plt.subplots()

correlation = df[
    ["math score", "reading score", "writing score"]
].corr()

sns.heatmap(correlation, annot=True, ax=ax)

st.pyplot(fig)


# Box Plot
st.header("Score Comparison")

fig, ax = plt.subplots()

sns.boxplot(
    data=df[
        ["math score", "reading score", "writing score"]
    ],
    ax=ax
)

st.pyplot(fig)


# Category Analysis
st.header("Performance Based on Test Preparation")

prep = df.groupby("test preparation course")[
    ["math score", "reading score", "writing score"]
].mean()

st.write(prep)
