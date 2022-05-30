from dataclasses import dataclass

from typing import NewType

Quantity = NewType("Quantity", int)
OrderReference = NewType("OrderReference", str)
ProductReference = NewType("ProductReference", str)


@dataclass(frozen=True)
class OrderLine:
    orderid: OrderReference
    sku: ProductReference
    qty: Quantity
