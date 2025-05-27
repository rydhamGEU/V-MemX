def fifo_page_replacement(pages, frames_count):
    memory = []
    index = 0
    page_faults = 0
    steps = []

    for page in pages:
        current_step = {"frame": list(memory), "page": page, "fault": False}

        if page not in memory:
            if len(memory) < frames_count:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames_count
            page_faults += 1
            current_step["fault"] = True

        current_step["frame"] = list(memory)
        steps.append(current_step)

    return steps, page_faults
