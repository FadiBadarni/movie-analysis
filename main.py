from neo4j_connector import Neo4jConnection
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Initialize Neo4j connection
conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# Sample Cypher query to fetch some data, e.g., all movies and their titles
query = """
MATCH (m:Movie)
RETURN m.title AS title, m.releaseDate AS releaseDate
ORDER BY m.releaseDate DESC
LIMIT 10
"""

results = conn.query(query)

for result in results:
    print(f"Movie Title: {result['title']}, Release Date: {result['releaseDate']}")

conn.close()
