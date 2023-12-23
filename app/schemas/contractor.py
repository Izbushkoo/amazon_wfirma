from typing import Optional

from pydantic import BaseModel, EmailStr


data = {"api":
    {
        "contractors": {
            "contractor": {
                "name": "test1",
                "city": "Warshaw",
                "zip": "12-345",
                "coutry": "PL",
                "tax_id_type": "custom",
                "nip": 1111111111
            }
        }
    }
}


class ContractorBase(BaseModel):

    id: str
    name: str
    city: str
    zip: str


class Contractor(ContractorBase):
    """Is the same for add and in base form"""
    street: str
    country: str
    tax_id_type: str
    nip: str
    seller: str
    buyer: str


