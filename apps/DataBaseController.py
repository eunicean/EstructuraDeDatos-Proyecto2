import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv('./.env')

neo4j_uri = os.getenv('NEO4J_URI')
neo4j_user = os.getenv('NEO4J_USER')
neo4j_password = os.getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

def create_favorite_connection(persona_name, juego_name):
    with driver.session() as session:
        session.write_transaction(lambda tx: create_relationship(tx, persona_name, juego_name))

def create_relationship(tx, persona_name, juego_name):
    query = "MATCH (p:Persona {nombre: $personaName}), (j:Juego {nombre: $juegoName}) " \
            "MERGE (p)-[:FAVORITE]->(j)"
    tx.run(query, personaName=persona_name, juegoName=juego_name)

def delete_favorite_connection(nombre_persona, nombre_juego):
    with driver.session() as session:
        session.write_transaction(lambda tx: delete_relationship(tx, nombre_persona, nombre_juego))

def delete_relationship(tx, nombre_persona, nombre_juego):
    query = "MATCH (p:Persona {nombre: $nombrePersona})-[f:FAVORITE]->(j:Juego {nombre: $nombreJuego}) " \
            "DELETE f"
    tx.run(query, nombrePersona=nombre_persona, nombreJuego=nombre_juego)