from uuid import UUID

import requests

from config import comment_prefix
from schemas.comments import Comment


def get_comments_by_post_id(post_id: UUID) -> list[Comment | str | None]:
    response = requests.get(comment_prefix + f"/post/{str(post_id)}")
    match response.status_code:
        case 200:
            response = response.json()
            if response:
                return list(map(lambda comment: Comment(**comment), response))
            return list()
        case _:
            return ["Failed to upload"]
