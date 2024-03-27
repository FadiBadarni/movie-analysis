import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(B):
    plt.figure(figsize=(40, 40))

    movies = [node for node, attr in B.nodes(data=True) if attr['bipartite'] == 0]
    cast = [node for node, attr in B.nodes(data=True) if attr['bipartite'] == 1]

    pos_movies = {}
    pos_cast = {}

    for index, movie in enumerate(movies):
        pos_movies[movie] = (1, -index * 2)

    for index, member in enumerate(cast):
        pos_cast[member] = (2, -index)

    pos = {**pos_movies, **pos_cast}

    nx.draw(B, pos, with_labels=True, node_size=1000,
            node_color=['skyblue' if node in movies else 'lightgreen' for node in B],
            font_size=10, alpha=0.6)

    plt.title('Bipartite Graph of Movies and Cast Members', fontsize=16)
    plt.axis('off')
    plt.show()


def visualize_genre_distribution(genre_movie_counts):
    genres = [item[0] for item in genre_movie_counts]
    counts = [item[1] for item in genre_movie_counts]

    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%\n({v:d})'.format(p=pct, v=val) if pct > 2 else ''

        return my_format

    wedges, texts, autotexts = ax.pie(counts, autopct=autopct_format(counts), startangle=140,
                                      colors=plt.cm.tab20.colors,
                                      textprops=dict(color="black", weight="bold", fontsize=8))

    centre_circle = plt.Circle((0, 0), 0.70, color='white', lw=0)
    fig.gca().add_artist(centre_circle)

    for autotext in autotexts:
        autotext.set_size('x-small')

    ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)

    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.80)

    plt.title('Distribution of Movie Genres', pad=20)
    ax.axis('equal')

    plt.show()


def visualize_movie_cast_counts(movie_count, cast_count):
    categories = ['Movies', 'Top 5 Popular Cast Members per Movie']
    counts = [movie_count, cast_count]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(categories, counts, color=['#1f77b4', '#ff7f0e'])

    max_count = max(counts)
    ax.set_ylim(0, max_count + max_count * 0.2)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

    ax.set_ylabel('Total Count')
    ax.set_title('Total Number of Movies and Top 5 Popular Cast Members Analyzed')
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def visualize_common_cast_graph(processed_data):
    B = nx.Graph()

    pos_movies = {}
    pos_cast = {}

    movie_count = sum(1 for movie in processed_data)
    movie_spacing = 20 / movie_count

    movie_index = 0
    for movie in processed_data:
        movie_title = movie['MovieTitle']
        B.add_node(movie_title, bipartite=0, type='movie')

        for cast_name in movie['CastNames']:
            if cast_name not in B:
                B.add_node(cast_name, bipartite=1, type='cast')
                pos_cast[cast_name] = (2, -len(pos_cast) * 2)
            B.add_edge(movie_title, cast_name)

        pos_movies[movie_title] = (1, -movie_spacing * movie_index)
        movie_index += 1

    pos = {**pos_movies, **pos_cast}

    plt.figure(figsize=(20, 20))
    nx.draw(B, pos, with_labels=True, node_size=3000,
            node_color=['skyblue' if attr['type'] == 'movie' else 'lightgreen' for node, attr in B.nodes(data=True)],
            font_weight='bold', font_size=9, alpha=0.6)

    plt.title('Bipartite Graph of Movies and Common Cast Members', fontsize=20)
    plt.axis('off')
    plt.show()
