def add_to_queue(p, queue=[]):
    queue.append(p)
    return queue
def can_seat(party_size, table_size):
    return party_size < table_size
def load_party(row):
    size = int(row[1])
    return {"pid": row[0], "size": sizee}
