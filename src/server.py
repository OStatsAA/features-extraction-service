"""Grpc Server"""

from concurrent import futures
import os
import grpc
import redis
from dotenv import load_dotenv
from src.database import FeaturesRepository

from src.service import Service, add_FeaturesExtractorServiceServicer_to_server


def serve() -> None:
    """Serving function"""
    db_conn = redis.Redis(os.environ.get("DATABASE_CONNECTION"))
    features_repository = FeaturesRepository(db_conn)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    add_FeaturesExtractorServiceServicer_to_server(
        Service(features_repository), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    load_dotenv()
    serve()
