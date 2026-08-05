# StockPilot

## StockPilot (Single-Store Inventory & Order Management API)


### Business Problem

    A small retail shop owner currently tracks stock in a spreadsheet. Stock counts drift from reality, staff oversell out-of-stock items, there's no audit trail of who changed what, and the owner has no visibility into order history or which products are slow-moving. StockPilot digitizes this: staff manage inventory and process orders through an API (a future frontend or POS integrates with it), the owner gets accurate stock and basic reporting.
    Requirements

### Functional

    CRUD for products, categories, suppliers.
    Stock adjustments (receive stock, manual correction) with a reason and audit trail — never allow silently overwriting a stock number.
    Create orders that decrement stock atomically; reject if insufficient stock; support partial fulfillment status.
    Two roles: owner (full access) and staff (can process orders and view stock, cannot delete products or view revenue reports).
    List/filter/paginate products and orders.
    Basic reporting: current stock value, low-stock list, orders in a date range.

### Non-functional

    Stock decrement on order creation must be safe under concurrent requests (two staff selling the last unit at the same time) — this is your first real encounter with transactions and row locking.
    p95 latency for product list under 150 requests/sec load (you'll actually load-test this in Week 4, lightly, with hey or locust).
    All destructive actions must be traceable to a user.
