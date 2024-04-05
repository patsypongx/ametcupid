def get_driver(headless=False):
    """
    Returns a Selenium WebDriver instance.

    Args:
        headless (bool): Whether to run the browser in headless mode.

    Returns:
        A Selenium WebDriver instance.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver
