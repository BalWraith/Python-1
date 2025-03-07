def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.
    
    :param text: The String to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then the specified width {1}"
                         .format(text, screen_width)) #ValueError 

    if text =="*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*",60)
banner_text("*",60)
banner_text("Dont stop believeing hold on to the ",60)
banner_text("feeling dont stop belieceing ",60)
banner_text("is",60)
banner_text(screen_width=60 )
banner_text("what",60)
banner_text("who",60)
banner_text("*",60)
banner_text("*",60)
banner_text("*",60)
