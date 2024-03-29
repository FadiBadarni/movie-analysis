# Movie Analytics with Neo4j and Python

This project provides a comprehensive analysis tool for exploring and understanding movie data using the Neo4j graph database and Python. It focuses on identifying influential cast members and their impact on movie success, analyzing genre distributions, and visualizing complex relationships within the movie industry.

## Features

- **Data Fetching**: Automated scripts to fetch movie data from Neo4j.
- **Analytics**: Advanced analytics to calculate centrality measures, compare success metrics, and select case study movies based on various criteria.
- **Data Processing**: Functions to process and normalize data, making it ready for analysis.
- **Visualization**: Multiple visualization techniques to represent data insights, including genre distribution, centrality measures, and the impact of influential cast members.

## Prerequisites

Before you get started, ensure you have the following installed:
- Python 3.x
- Neo4j Database
- Required Python packages: `networkx`, `pandas`, `matplotlib`, `seaborn`, `numpy`, `adjustText`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/FadiBadarni/movie-analysis.git
   cd movie-analysis
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Ensure you have the following environment variables set up for your Neo4j connection:

   - `NEO4J_URI`: Your Neo4j database URI.
   - `NEO4J_USER`: Your Neo4j database username.
   - `NEO4J_PASSWORD`: Your Neo4j database password.

   You can set these variables in a `.env` file or export them directly in your shell.

## Usage

The project is structured into multiple Python scripts, each serving a different purpose in the data analysis pipeline:

- **`data_fetcher.py`**: Contains functions to fetch movie data and related information from Neo4j.
- **`data_process.py`**: Provides data processing and normalization functions to prepare data for analysis.
- **`graph_builder.py`**: Includes functions to build bipartite graphs for movies and cast members.
- **`visualization.py`**: Contains various functions to visualize data insights graphically.

