from pydantic import BaseModel

class ConstructionRegulationBase(BaseModel):
    code: str
    name: str
    action: str

class ConstructionRegulationCreate(ConstructionRegulationBase):
    pass

class ConstructionRegulationUpdate(ConstructionRegulationBase):
    pass

class ConstructionRegulationOut(ConstructionRegulationBase):
    id: int

    class Config:
        orm_mode = True
