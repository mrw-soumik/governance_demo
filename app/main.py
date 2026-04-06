from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI(
    title="Governance Demo API",
    description="A small startup-style backend used to demonstrate development governance controls.",
    version="1.0.0",
)


class Project(BaseModel):
    id: int
    name: str
    owner: str
    status: str
    risk_level: str


PROJECTS = [
    Project(id=1, name="Website Redesign", owner="Product Team", status="active", risk_level="medium"),
    Project(id=2, name="Customer Portal", owner="Engineering", status="active", risk_level="low"),
    Project(id=3, name="Legacy Cleanup", owner="Platform Team", status="planned", risk_level="high"),
]


@app.get("/")
def read_root():
    return {
        "message": "Governance Demo API is running",
        "docs": "/docs",
        "health": "/health",
        "projects": "/projects",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/projects", response_model=List[Project])
def list_projects(
    status: Optional[str] = Query(default=None, description="Filter projects by status"),
):
    if status is None:
        return PROJECTS
    return [project for project in PROJECTS if project.status.lower() == status.lower()]
