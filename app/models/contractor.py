from typing import Optional

from sqlmodel import Field, SQLModel

contractor = {"contractor": {
                "id": "107736311",
                "name": "SHENZHENSHI YIXIANG KEJI YOUXIAN GONGSI",
                "zip": "518000",
                "country": "CN",
                "tax_id_type": "nip",
                "nip": "5263339968",
                "contact_name": "Shen zhen shi yi xiang ke ji you xian gong si",
                "contact_zip": "518000",
                "contact_country": "CN",
                "buyer": "0",
                "seller": "1",
                "remind": "0",
                "source": "Własne",
                "account_number": "",
    }
}


class Contractor(SQLModel, table=True):
    __tablename__ = "contractors"

    id: str = Field(default=None, primary_key=True)
    name: str
    street: str
    city: str
    zip: str
    country: str
    tax_id_type: str
    nip: str
    seller: str
    buyer: str


