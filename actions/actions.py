import json

from robocorp.actions import action
from robocorp import browser

@action
def search_books(topic: str, count: int) -> str:
    """Searches for books based on a topic

    Keyword arguments:
    topic -- Topic to search books on
    count -- Number of books to retrieve
    """
    browser.configure(browser_engine="chromium", headless=False)

    page = browser.goto("https://google.com/?hl=en")

    # accept popup in europe
    # page.click("text='Accept all'")

    page.fill("textarea[name='q']", f"{topic} books")
    page.press("textarea[name='q']", "Enter")

    page.click("text='Books'")
    page.wait_for_selector("h3")

    title_elements = page.query_selector_all("h3")
    titles = [element.text_content() for element in title_elements]

    description_elements = page.query_selector_all("div>div>span>span")
    descriptions = [element.text_content() for element in description_elements]

    link_elements = page.query_selector_all("div>span>a[data-ved][href]")
    links = [element.get_attribute("href") for element in link_elements]

    items = [
        {"title": t, "description": d, "link": l}
        for t, d, l in zip(titles, descriptions, links)
    ]

    return json.dumps(items[:count])
