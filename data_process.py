import pandas as pd


def process_movies_data(movies_data):
    normalized_data = []
    for record in movies_data:
        for cast_name in record['CastNames']:
            normalized_data.append({
                'MovieTitle': record['MovieTitle'],
                'ReleaseDate': record['ReleaseDate'],
                'CastName': cast_name
            })

    df = pd.DataFrame(normalized_data)

    common_casts = df.groupby('CastName').filter(lambda x: len(x['MovieTitle'].unique()) > 1)

    final_movies_data = []
    for title, group in common_casts.groupby('MovieTitle'):
        unique_casts = group['CastName'].unique().tolist()

        final_movies_data.append({
            'MovieTitle': title,
            'ReleaseDate': group['ReleaseDate'].iloc[0],
            'CastNames': unique_casts
        })

    return final_movies_data
