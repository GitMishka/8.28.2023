def deduplicate(users):
    seen_ids = set()
    deduplicated_users = []

    for user in users:
        if user['id'] not in seen_ids:
            seen_ids.add(user['id'])
            deduplicated_users.append(user)

    return deduplicated_users
