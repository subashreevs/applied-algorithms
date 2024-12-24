import heapq  # Import heapq for efficient heap-based priority queue operations

def rajsTradingShowdown(order_list: list[list[int]]) -> int:
    MODULO_CONSTANT = 10**9 + 7  # Modulo to prevent overflow and ensure result stays within bounds
    buy_order_heap = []  # Max heap for buy orders (using negative prices to simulate max heap behavior)
    sell_order_heap = []  # Min heap for sell orders

    # Process each order in the provided list
    for order_price, order_amount, order_type in order_list:
        # Check if the order is a buy order
        if order_type == 0:  # Buy order
            # Match buy order with existing sell orders if the price meets conditions
            while order_amount > 0 and sell_order_heap and sell_order_heap[0][0] <= order_price:
                # Access the lowest sell price available
                current_sell_price, current_sell_amount = heapq.heappop(sell_order_heap)
                
                # Check if current sell order can fully meet the buy order amount
                if current_sell_amount > order_amount:
                    # Partially fulfill the buy order, push remaining amount back to the sell heap
                    heapq.heappush(sell_order_heap, (current_sell_price, current_sell_amount - order_amount))
                    order_amount = 0  # Set amount to zero as buy order is fully matched
                else:
                    # Fully consume the current sell order, reduce buy order amount accordingly
                    order_amount -= current_sell_amount
            
            # If there’s still amount left to fulfill in the buy order, add it to the buy heap
            if order_amount > 0:
                heapq.heappush(buy_order_heap, (-order_price, order_amount))
        
        else:  # Sell order processing
            # Match sell order with existing buy orders if price conditions are met
            while order_amount > 0 and buy_order_heap and -buy_order_heap[0][0] >= order_price:
                # Access the highest buy price available (using negative for max heap)
                current_buy_price, current_buy_amount = heapq.heappop(buy_order_heap)
                
                # Check if current buy order can fully meet the sell order amount
                if current_buy_amount > order_amount:
                    # Partially fulfill the sell order, push remaining amount back to the buy heap
                    heapq.heappush(buy_order_heap, (current_buy_price, current_buy_amount - order_amount))
                    order_amount = 0  # Set amount to zero as sell order is fully matched
                else:
                    # Fully consume the current buy order, reduce sell order amount accordingly
                    order_amount -= current_buy_amount
            
            # If there’s still amount left to fulfill in the sell order, add it to the sell heap
            if order_amount > 0:
                heapq.heappush(sell_order_heap, (order_price, order_amount))

    # Calculate the total remaining buy and sell orders that couldn't be matched
    total_remaining_orders = sum(amount for _, amount in buy_order_heap) + sum(amount for _, amount in sell_order_heap)
    # Return the result modulo the constant to prevent overflow
    return total_remaining_orders % MODULO_CONSTANT

# # Example usage
# order_example_1 = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
# print(rajsTradingShowdown(order_example_1))  # Expected output: 6

# order_example_2 = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
# print(rajsTradingShowdown(order_example_2))  # Expected output: 999999984