import pandas as pd
import glob

# Опрацювання постів (submissions)
print("**** ОБ'ЄДНАННЯ ПОСТІВ (SUBMISSIONS) ****")
post_files = glob.glob('data/RS_*.csv')
print(f"Знайдено файлів постів для об'єднання: {len(post_files)}")

if post_files:
    posts_list = []
    for f in post_files:
        df = pd.read_csv(f, low_memory=False)
        posts_list.append(df)

    posts_df = pd.concat(posts_list, ignore_index=True)
    
    # Очищення від дублікатів
    if 'id' in posts_df.columns:
        initial_rows = len(posts_df)
        posts_df = posts_df.drop_duplicates(subset=['id'])
        print(f"Видалено дублікатів (пости): {initial_rows - len(posts_df)}")
    
    posts_df.to_csv('data/final_submissions.csv', index=False)
    print("Файл data/final_submissions.csv успішно збережено!\n")
else:
    print("Файли постів (RS_*.csv) не знайдені.\n")


# Опрацювання коментарів (comments)
print("**** ОБ'ЄДНАННЯ КОМЕНТАРІВ (COMMENTS) ****")
comment_files = glob.glob('data/RC_*.csv')
print(f"Знайдено файлів коментарів для об'єднання: {len(comment_files)}")

if comment_files:
    comments_list = []
    for f in comment_files:
        df = pd.read_csv(f, low_memory=False)
        comments_list.append(df)

    comments_df = pd.concat(comments_list, ignore_index=True)
    
    # Очищення від дублікатів
    if 'id' in comments_df.columns:
        initial_rows = len(comments_df)
        comments_df = comments_df.drop_duplicates(subset=['id'])
        print(f"Видалено дублікатів (коментарі): {initial_rows - len(comments_df)}")
    
    comments_df.to_csv('data/final_comments.csv', index=False)
    print("Файл data/final_comments.csv успішно збережено!\n")
else:
    print("Файли коментарів (RC_*.csv) не знайдені.\n")