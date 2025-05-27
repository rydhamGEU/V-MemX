from collections import OrderedDict

def lru_page_replacement(pages, frames_count):
    cache = OrderedDict()
    steps = []
    page_faults = 0

    for page in pages:
        step = {"page": page, "frame": list(cache.keys()), "fault": False}

        if page in cache:
            # Move the page to the end (most recently used)
            cache.move_to_end(page)
        else:
            # Page fault occurred
            page_faults += 1
            step["fault"] = True
            if len(cache) >= frames_count:
                # Remove least recently used page (first item)
                cache.popitem(last=False)
            cache[page] = True  # Value doesn't matter

        step["frame"] = list(cache.keys())
        steps.append(step)

    return steps, page_faults
