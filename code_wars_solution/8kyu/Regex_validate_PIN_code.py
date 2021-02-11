def validate_pin(pin):
    pin_list = [int(num) for num in pin if pin.isdigit()]
    return len(pin_list) == 4 or len(pin_list) == 6