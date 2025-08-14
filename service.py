from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_items(db: Session):

    query = db.query(models.Items)

    items_all = query.all()
    items_all = (
        [new_data.to_dict() for new_data in items_all] if items_all else items_all
    )

    raise HTTPException(status_code=469, detail="Error Message")

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {},
    }
    return res
