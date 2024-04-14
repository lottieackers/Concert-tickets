import requests
import json

def get_tour_by_date(date):
    result = requests.get(
        'http://127.0.0.1:5001/tours/{}'.format(date),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def display_tour(records):
    print("{:<15} {:<20} {:<15}  ".format(
        'Artist', 'Date', 'Tickets Available'))
    print('-' * 50)

    # print each data item.
    for item in records:
        date_str = item['tour_date'][:16]
        print("{:<15} {:<20} {:<15} ".format(
            item['artist'], date_str, item['tickets_available']
        ))



def run():
    print("Welcome to CFG Arena's last minute bookings!")
    print()
    date = input('What date would you like to book a concert for? (YYYY-MM-DD): ')
    print()
    tours = get_tour_by_date(date)

    if tours:
        print("The tours available with the selected date are: ")
        print()
        display_tour(tours)
    else:
        print("No tours are available for the selected dates.")


    # print('####### AVAILABILITY #######')
    # print()
    # display_availability(tours)
    # print()
    # place_booking = input('Would you like to book an appointment (y/n)?  ')


if __name__ == '__main__':
    run()