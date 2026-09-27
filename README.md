# CSS_Olympics_Project

This project contains all code used to analyse data about Olympic sports.

# 1. Reddit Data Processing and Analysis

Files `task2_exploration.py` and `merge.py` are designed to merge, clean, and perform basic analysis on Reddit text data (submissions and comments) stored in CSV format.

## Structure

For the scripts to run correctly, place your raw source files inside a `data/` folder in the root directory:
*   `data/RS_*.csv` — Raw files containing Reddit submissions (posts).
*   `data/RC_*.csv` — Raw files containing Reddit comments.

## Script Overview

### 1. Data Merging and Cleaning (`merge.py`)
This script aggregates scattered CSV files, merges them, and removes duplicate entries to prepare the dataset for analysis.

**Key Features:**
*   Locates all files matching the `RS_*.csv` and `RC_*.csv` patterns using the `glob` module.
*   Combines them into two consolidated DataFrames using `pandas.concat`.
*   Identifies and drops duplicate entries based on the unique `id` column.
*   Saves the cleaned, final datasets as:
    *   `data/final_submissions.csv`
    *   `data/final_comments.csv`

### 2. Final Data Analysis (`task2_exploration.py`)
This script is used to quickly inspect and generate summary statistics for the compiled final datasets.

**Key Features:**
*   Verifies the existence of the final aggregated CSV files.
*   Calculates and prints the physical file size on disk in Megabytes (MB).
*   Displays the total row counts (total submissions and comments).
*   Computes and displays the data distribution across different subreddits (`subreddit` value counts).
*   Prints a preview (`.head()`) of the data rows for structure verification.

##Requirements & Usage

This project requires Python and the **Pandas** library.

1. Install the required dependency if you haven't already:
   ```bash
   pip install pandas
   ```

2. Run the merging script first to combine your raw source files:
   ```bash
   python merge.py
   ```

3. Run the analysis script next to view metrics and verify your data:
   ```bash
   python task2_exploration.py
   ```