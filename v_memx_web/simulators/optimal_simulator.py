def optimal_page_replacement(pages, frames_count):
    memory = []
    page_faults = 0
    steps = []

    for i in range(len(pages)):
        page = pages[i]
        step = {"page": page, "frame": list(memory), "fault": False}

        if page not in memory:
            if len(memory) < frames_count:
                memory.append(page)
            else:
                # Find the page in memory that is used farthest in future
                future = pages[i + 1 :]
                indices = []

                for mem_page in memory:
                    if mem_page in future:
                        index = future.index(mem_page)
                    else:
                        index = float("inf")  # Never used again
                    indices.append(index)

                # Choose the page with max index (used last or never)
                to_replace = indices.index(max(indices))
                memory[to_replace] = page

            page_faults += 1
            step["fault"] = True

        step["frame"] = list(memory)
        steps.append(step)

    return steps, page_faults
