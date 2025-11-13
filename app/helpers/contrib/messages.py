from django.contrib import messages


def set_single_message(request, level, text: str) -> None:
    """
    Remove all exisiting messages and add only one
    
    Args:
        request: HttpRequest from the view
        level: type of message (error, success, warning, info)
        text: message to be displayed
    Returns:
        None
    """

    storage = messages.get_messages(request)
    for _ in storage:
        pass

    messages.add_message(request, level, text)
