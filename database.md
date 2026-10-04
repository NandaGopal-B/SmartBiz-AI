# Database Design

## customers
Stores customer profile, value and engagement information.

## products
Stores product catalog and stock.

## sales
Stores transactional sales information.

For production use, `customer_id` and `product_id` should be configured as foreign keys with appropriate indexing and transaction constraints.
