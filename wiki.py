import json
import sys
from wikipediaapi import Wikipedia

from typing import Dict, List


def get_data(wiki: Wikipedia, title: str) -> Dict[str, str] | None:
    page = wiki.page(title)
    if not page.exists():
        return None
    return {"title": page.title, "summary": page.summary, "url": page.fullurl}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input")
        quit()

    wiki = Wikipedia("en")

    with open("data.json", "w") as f:
        json.dump([get_data(wiki, title) for title in sys.argv[1:]], f)
