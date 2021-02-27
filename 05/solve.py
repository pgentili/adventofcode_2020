def get_seat_location(seat_code):
    row_str = seat_code[:7].replace('F', '0').replace('B', '1')
    col_str = seat_code[7:].replace('L', '0').replace('R', '1')

    return int(row_str, 2), int(col_str, 2)

def get_seat_id(seat_code):
    return int(
        seat_code.replace('F', '0')
                 .replace('B', '1')
                 .replace('L', '0')
                 .replace('R', '1'),
        2
    )

    

if __name__ == '__main__':
    with open('input.txt') as f:
        seat_codes = f.read().splitlines()
    seat_ids = [get_seat_id(seat_code) for seat_code in seat_codes]
    seat_ids.sort()
    print(seat_ids[-1])

    for prev, next in zip(seat_ids[:-1], seat_ids[1:]):
        if next - prev == 2:
            print(prev + 1)