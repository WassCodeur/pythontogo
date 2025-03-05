from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Speaker(BaseModel):
    name: str
    title: str
    image_url: str


class ScheduleItem(BaseModel):
    time: str
    title: str
    description: Optional[str] = None


class Event(BaseModel):
    id: int
    title: str
    description: str
    short_description: str
    category: str
    date: str
    time: str
    location: str
    venue_address: Optional[str] = None
    image_url: str
    status: str  # "upcoming", "ongoing", or "past"
    speakers: Optional[List[Speaker]] = []
    schedule: Optional[List[ScheduleItem]] = []
