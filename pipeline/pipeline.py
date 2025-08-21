from src.vector_store import VectorStoreBuilder
from src.recommender import MovieRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.exception import CustomException
logger = get_logger(__name__)

class MovieRecommendationPipeline:
    def __init__(self,persist_dir="/home/user/Documents/movie_recommander/chroma_db"):
        try:
            logger.info("Intializing Recommdation Pipeline")
            
            vector_builder = VectorStoreBuilder(csv_path="" , persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = MovieRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
        


        