from typing import Dict, Any

from . import models


def course_item_serializer(course_item=models.CourseItem) -> Dict[str, Any]:
    return {
        "episode_title": course_item.episode_title,
        "episode_url": course_item.episode_url,
        "episode": course_item.episode,
        "episode_note": course_item.episode_note,
        "episode_archive": course_item.episode_archive,
        "published": course_item.published,
        "created": course_item.created,
        "last_updated": course_item.last_updated,
    }
