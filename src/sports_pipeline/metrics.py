def ip_to_outs(ip: str) -> int:
    """Convert Innings Pitched (IP) to total Outs.
    The IP notation isn't decimal: The integer part represents complete innings, 
    and the digit after the
    decimal point represents additional outs (.0, .1, and .2).
    Therefore, "158.1" means 1  58 1/3 innings, not the decimal number 158.1,
    and converting the string with float() produces incorrect results.

    Args:
        ip: Innings pitched in the format returned by the MLB Stats API,
            for example, "158.2".

    Returns:
        The total number of outs recorded by the pitcher.

    Examples:
        >>> ip_to_outs("158.0")
        474
        >>> ip_to_outs("158.2")
        476
    """
    integer_text, decimal_text = ip.split(".")

    complete_innings = int(integer_text)
    additional_outs = int(decimal_text)
    if additional_outs not in (0, 1, 2):
        raise ValueError("Additional outs must be 0, 1, or 2")
    return complete_innings * 3 + additional_outs

def era(er: int, outs: int) -> float | None:
    """Calculate the pitcher's earned run average (ERA) using outs
    instead of Innings Pitched.
    
    Notes:
            9 Innings equal 27 outs.
    
    Args:
        er: Is any run that scores against a pitcher without 
            the benefit of an error or a passed ball.
        outs: Is recorded when a player at bat or a baserunner 
            is retired by the team in the field.  

    Returns:
        Returns the pitcher's ERA: a decimal value representing the average 
        earned runs allowed per 27 outs recorded or None if outs is zero.   
    
    Example:
        >>> era(7, 0)
        None
        >>> era(77, 553)
        3.759493670886076
    """
    if outs == 0:
        return None
    return (er * 27) / outs 

