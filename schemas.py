from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Items(BaseModel):
    detail: Optional[str]=None


class ReadItems(BaseModel):
    detail: Optional[str]=None
    class Config:
        from_attributes = True


