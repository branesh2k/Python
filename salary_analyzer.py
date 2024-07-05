
def calculate_salary(base_salary, bonus_rate=0.1):
    """
    Calculate the total salary including the bonus.

    This function calculates the total salary by adding a bonus to the base salary. 
    The bonus is a percentage of the base salary, defined by the bonus rate.

    Parameters:
    base_salary (float): The base salary amount.
    bonus_rate (float, optional): The bonus rate as a decimal (default is 0.1, which represents 10%).

    Returns:
    float: The total salary including the bonus.
    """
    return base_salary * (1 + bonus_rate)
