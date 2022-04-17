import datetime

from homeapp.models import BookingRooms


def availability(rooms, check_in, check_out):
    avail_list = []
    booking_list = BookingRooms.objects.filter(room = rooms)
    
    for bookings in booking_list:
        print(type(bookings.check_in),type(check_in),type(bookings.check_out),type(check_out))
        if bookings.check_in > check_out or bookings.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)