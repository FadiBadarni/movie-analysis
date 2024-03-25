import os

from dotenv import load_dotenv

from neo4j_connector import Neo4jConnection


def fetch_movie_data():
    # Ensure environment variables are loaded (redundant if already loaded in main.py, but safe)
    load_dotenv()

    # Extract Neo4j credentials
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Initialize and use the Neo4j connection within a context manager for automatic cleanup
    try:
        with Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD) as conn:
            query = """
            MATCH (m:Movie)-[r:HAS_CAST]->(c:Cast), (m)-[s:HAS_CREW]->(cr:Crew)
            RETURN m.title AS movie, collect(c.name) AS cast, collect(cr.name) AS crew
            LIMIT 10
            """
            results = conn.query(query)
            return results
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return []
