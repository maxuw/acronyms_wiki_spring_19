# link extractor class


def type_page(url):

    if "pl.wikipedia.org" not in url:

        return "not a polish wikipedia page"

    if "https://" in url:
        url = url.replace("https://", "")

    elif "http://" in url:
        url = url.replace("http://", "")

    if "www." in url:
        url = url.replace("www.", "")

    url = url.replace("pl.wikipedia.org/", "")

    if "wiki/" not in url:

        return "wikipedia, but not an encyclopedia type of page"

    else:
        url = url.replace("wiki/", "")

        print(url)

        if "Kategoria:" in url:

            return "category"

        elif "Portal:" in url:

            return "portal_page"

        elif ":" not in url:
            return "record_page"

        else:
            return "unknown type of page"
