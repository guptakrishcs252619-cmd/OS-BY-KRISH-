from collections import deque

def fifo_page_replacement(pages, frames):
    memory = []
    queue = deque()
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                old_page = queue.popleft()
                memory.remove(old_page)
                memory.append(page)
                queue.append(page)

        print("Page:", page, "Memory:", memory)

    return hits, misses


def lru_page_replacement(pages, frames):
    memory = []
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            misses += 1

            if len(memory) >= frames:
                memory.pop(0)

            memory.append(page)

        print("Page:", page, "Memory:", memory)

    return hits, misses


pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))


fifo_hits, fifo_misses = fifo_page_replacement(pages, frames)


lru_hits, lru_misses = lru_page_replacement(pages, frames)

total = len(pages)



print("FIFO Hits:", fifo_hits)
print("FIFO Misses:", fifo_misses)
print("FIFO Hit Ratio:", round(fifo_hits / total, 2))
print("FIFO Miss Ratio:", round(fifo_misses / total, 2))

print("\nLRU Hits:", lru_hits)
print("LRU Misses:", lru_misses)
print("LRU Hit Ratio:", round(lru_hits / total, 2))
print("LRU Miss Ratio:", round(lru_misses / total, 2))
print ("krish 085")
