from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import DbConfig

db_config = DbConfig()
async_engine = create_async_engine(db_config.database_url, echo=True)

async_session_maker = async_sessionmaker(bind=async_engine)
