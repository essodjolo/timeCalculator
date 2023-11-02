import time_calculator
import test_module

if __name__ == '__main__':
    print("Running unit tests...")

    exec("test_module")

    testing = test_module.MyTestCase()

    testing.test_convert_time_to_12h_format()
    testing.test_convert_time_to_24h_format()
    testing.test_add_time()
    testing.test_wrong_duration()
    testing.test_wrong_starting_day_of_the_week()
