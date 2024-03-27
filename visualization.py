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
    # Prepare data
    genres = [item[0] for item in genre_movie_counts]
    counts = [item[1] for item in genre_movie_counts]

    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

    # Function to only display percentages above a certain threshold, for readability
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%\n({v:d})'.format(p=pct, v=val) if pct > 2 else ''

        return my_format

    # Create the pie chart
    wedges, texts, autotexts = ax.pie(counts, autopct=autopct_format(counts), startangle=140,
                                      colors=plt.cm.tab20.colors,
                                      textprops=dict(color="black", weight="bold", fontsize=8))

    # Draw a circle at the center to make it a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, color='white', lw=0)
    fig.gca().add_artist(centre_circle)

    # Adjust the position of the percentage labels to avoid overlap
    for autotext in autotexts:
        autotext.set_size('x-small')  # Adjusting the text size
        # Further adjustments to text positioning could be made here if necessary

    # Add a legend outside the chart
    ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)

    # Adjust layout
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.80)

    # Title and equal aspect ratio for the pie chart
    plt.title('Distribution of Movie Genres', pad=20)
    ax.axis('equal')  # Ensures pie chart is drawn as a circle

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
    # Create a new graph
    B = nx.Graph()

    # Initialize positions dictionaries
    pos_movies = {}
    pos_cast = {}

    # Count the number of movies for even distribution
    movie_count = sum(1 for movie in processed_data)
    movie_spacing = 20 / movie_count  # Adjust spacing based on your preference or graph size

    # Create a node for each movie and cast member, and add edges between them
    movie_index = 0  # To track the current movie index for positioning
    for movie in processed_data:
        movie_title = movie['MovieTitle']
        B.add_node(movie_title, bipartite=0, type='movie')

        for cast_name in movie['CastNames']:
            if cast_name not in B:
                B.add_node(cast_name, bipartite=1, type='cast')
                # Stack cast nodes vertically with consistent gaps
                pos_cast[cast_name] = (2, -len(pos_cast) * 2)  # Adjust as needed
            B.add_edge(movie_title, cast_name)

        # Position movie nodes with even spacing
        pos_movies[movie_title] = (1, -movie_spacing * movie_index)
        movie_index += 1  # Move to the next index for the next movie

    # Combine positions
    pos = {**pos_movies, **pos_cast}

    # Draw the graph
    plt.figure(figsize=(20, 20))
    nx.draw(B, pos, with_labels=True, node_size=3000,
            node_color=['skyblue' if attr['type'] == 'movie' else 'lightgreen' for node, attr in B.nodes(data=True)],
            font_weight='bold', font_size=9, alpha=0.6)

    plt.title('Bipartite Graph of Movies and Common Cast Members', fontsize=20)
    plt.axis('off')
    plt.show()

