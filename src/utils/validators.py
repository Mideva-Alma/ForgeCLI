def find_by_name(records, name):
    name_lower = name.strip().lower()
    for record in records:
        if record["name"].strip().lower() == name_lower:
            return record
    return None


def find_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None