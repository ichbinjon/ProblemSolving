# Complete the function below.

def  getMinPrice(requiredSeats, seatPrices):
    # -1 as a placeholder value
    min = -1
    for x in seatPrices:
        free_seats = check_row_x(requiredSeats, x)
        if not free_seats:
            continue
        else:
            for y in free_seats:
                seats = x[y-requiredSeats+1:y+1]
                print(seats)
                total_price = get_total_price(seats)
                if (total_price < min or min == -1):
                    min = total_price
    return min
    
def check_row_x (requiredSeats, row):
    counter = 0
    seat_list = []
    for index, x in enumerate(row):
        if(x != -1):
            counter = counter + 1
            if (counter >= requiredSeats): #appends the last needed seat in the row
                seat_list.append(index)
        else:
            counter = 0
    return seat_list

def get_total_price (row):
    total_price = 0
    for x in row:
        total_price = total_price + x
    return total_price
        
                            
                
                        
                