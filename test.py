from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

item = Item(name="이동윤", price=1000)

print(dict(item))
d_item = dict(item)
print(d_item)
print(*d_item)
result = {'item_id': "Hello World", **d_item}
print(result)
