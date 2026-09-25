# Don't name the folder types, because Python's standard library
# already has a types module. If a folder named types ever ends
# up first on Python's module search path, it hides the real one
# and imports across the app break with confusing errors.

from app.schemas.req_res import ApiResponse

__all__ = ["ApiResponse"]
