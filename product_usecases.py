import uuid
from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, get_many


def product_create(name: str, price: float):
    product = Product(
        id=str(uuid.uuid4()),
        name=name,
        price=price,
    )
    save(product)

    return product


def product_get_by_id(id: str) -> Optional[Product]:
    # raise Exception('Not implemented yet')
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    # raise Exception('Not implemented yet')
    return get_many(page=page, limit=limit)
