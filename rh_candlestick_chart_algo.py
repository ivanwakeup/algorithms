
#algorithm from robinhood interview asking to construct a candlestick chart (financial chart in trading use to show open/close/min/max prices of a stock). 
#input represents trades at a given [price, time]
#if there is a window with no trades, use the last close price as open,close,min,max!
trades = [
    [1, 0],
    [2, 4],
    [4, 11],
    [3, 30]
]
# [start_time_block, open_price, close_price, max_price, min_price]
expected_output = [[0, 1, 2, 2, 1], [10, 4, 4, 4, 4], [20, 4, 4, 4, 4] ,[30, 3, 3, 3 ,3]]

'''
create array that keeps track of values for current time window. initialize current window with first input trade pair.
when we encounter a new window, update result and re-init array for current window

init cur_result as 
while stuff_to_process:
    while cur_idx and time in cur_window
    set last seen value

'''
def get_price_aggregates(trades_arr):
    blocks = {}
    has_values = set()

    max_time = trades_arr[-1][1]

    for idx in range(0, max_time+1, 10):
        blocks[idx] = [idx, 0, 0, -9999, 9999]
    
    for item in trades_arr:
        price = item[0]
        time = item[1]

        block = time//10*10
        has_values.add(block)

        if not blocks[block][0]:
            blocks[block][0] = price
        
        blocks[block][1] = price
        blocks[block][2] = max(blocks[block][2], price)
        blocks[block][3] = min(blocks[block][2], price)

    
    for key in blocks.keys():
        if key not in has_values:
            prev_key = key-10
            blocks[key] = [block, blocks[prev_key][1], blocks[prev_key][1], blocks[prev_key][1],blocks[prev_key][1]]
    
    return blocks

        




            


