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
    import matplotlib.pyplot as plt

    # Prepare data
    genres = [item[0] for item in genre_movie_counts]
    counts = [item[1] for item in genre_movie_counts]

    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

    # Function to only display percentages above a certain threshold, for readability
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%\n({v:d})'.format(p=pct,v=val) if pct > 2 else ''
        return my_format

    # Create the pie chart
    wedges, texts, autotexts = ax.pie(counts, autopct=autopct_format(counts), startangle=140, colors=plt.cm.tab20.colors, textprops=dict(color="black", weight="bold", fontsize=8))

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


