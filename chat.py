from datetime import datetime

class YourClass:
    def get_day_difference(self, date_str):
        # Convert the input date string to a datetime object
        input_date = datetime.strptime(date_str, '%Y-%m-%d')

        # Get today's date
        today = datetime.today()

        # Calculate the difference between the input date and today's date
        difference = input_date - today

        # Return the difference in days
        return difference.days

# Example usage
your_instance = YourClass()
print(your_instance.get_day_difference('2024-02-20'))  # Output will be the difference in days between '2024-02-20' and today
