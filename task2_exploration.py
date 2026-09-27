import pandas as pd
import os

print("**** АНАЛІЗ ФІНАЛЬНИХ ДАНИХ ****")

# Аналіз постів (submissions)
if os.path.exists('data/final_submissions.csv'):
    print("\n**** ПОСТИ (SUBMISSIONS) ****")
    posts_df = pd.read_csv('data/final_submissions.csv', low_memory=False)
    
    size_mb_posts = os.path.getsize('data/final_submissions.csv') / (1024 * 1024)
    print(f"a) Загальний розмір файлу постів: {size_mb_posts:.2f} MB")
    print(f"b) Кількість рядків (постів): {len(posts_df)}")
    print("\nd) Розподіл постів за сабреддітами:")
    if 'subreddit' in posts_df.columns:
        print(posts_df['subreddit'].value_counts())
        
    print("\n*** Приклад даних постів ***")
    print(posts_df.head())
else:
    print("\nФайл 'data/final_submissions.csv' не знайдено.")

print("\n" + "*"*60)

# Аналіз коментарів (comments)
if os.path.exists('data/final_comments.csv'):
    print("\n**** КОМЕНТАРІ (COMMENTS) ****")
    comments_df = pd.read_csv('data/final_comments.csv', low_memory=False)
    
    size_mb_comments = os.path.getsize('data/final_comments.csv') / (1024 * 1024)
    print(f"a) Загальний розмір файлу коментарів: {size_mb_comments:.2f} MB")
    print(f"b) Кількість рядків (коментарів): {len(comments_df)}")
    print("\nd) Розподіл коментарів за сабреддітами:")
    if 'subreddit' in comments_df.columns:
        print(comments_df['subreddit'].value_counts())
        
    print("\n*** Приклад даних коментарів ***")
    print(comments_df.head())
else:
    print("\nФайл 'data/final_comments.csv' не знайдено.")