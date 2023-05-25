import pandas as pd
import json

# Example JSON data
data = '''
[
    {
        "id": 1,
        "name": "John Doe",
        "languages": [
            {
                "name": "Python",
                "experience": "Intermediate"
            },
            {
                "name": "Java",
                "experience": "Advanced"
            }
        ],
        "skills": ["Data Analysis", "Machine Learning", "Web Development"]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "languages": [
            {
                "name": "JavaScript",
                "experience": "Intermediate"
            },
            {
                "name": "C++",
                "experience": "Beginner"
            }
        ],
        "skills": ["Data Science", "Data Visualization"]
    },
    {
        "id": 3,
        "name": "Alice Brown",
        "languages": [
            {
                "name": "Python",
                "experience": "Advanced"
            },
            {
                "name": "JavaScript",
                "experience": "Intermediate"
            }
        ]
    }
]
'''

# Load JSON data into a Python list
json_data = json.loads(data)

# Normalize the JSON data (including skills and languages)
df = pd.json_normalize(json_data,
                       record_path=['languages'],
                       meta=['id', 'name'],
                       meta_prefix='person_',
                       record_prefix='language_')

# Check if 'person_skills' column exists in the DataFrame
if 'person_skills' in df.columns:
    # Separate the skills into different columns
    df = df.join(pd.DataFrame(df.pop('person_skills').tolist()).add_prefix('skill_'))

# Check if 'language_name' column exists in the DataFrame
if 'language_name' in df.columns:
    # Separate the languages into different columns
    df = df.join(pd.DataFrame(df.pop('language_name').tolist()).add_prefix('language_'))
    df['language_experience'] = df['language_experience'].apply(lambda x: [i.get('experience') for i in x])
    df = df.join(pd.DataFrame(df.pop('language_experience').tolist()).add_prefix('language_experience'))

# Print the resulting DataFrame
print(df)