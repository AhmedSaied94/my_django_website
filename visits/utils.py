def get_visitor_info(request):
    """
    get the visitor info from the request
    ip_address: the ip address of the visitor
    os: the operating system of the visitor
    browser: the browser of the visitor
    device: the device of the visitor
    """
    user_ip = request.headers.get("User-IP")
    ip_address = user_ip or request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR")).split(",")[0]
    os = request.user_agent.os.family
    browser = request.user_agent.browser.family
    device = request.user_agent.device.family
    return ip_address, os, browser, device
