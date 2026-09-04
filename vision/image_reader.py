from pathlib import Path


class ImageReader:

    def analyze(self, image_path):

        path = Path(image_path)

        if not path.exists():
            return {
                "success": False,
                "error": "Image not found."
            }

        return {
            "success": True,
            "message": "Image received. Vision engine will be added."
        }
