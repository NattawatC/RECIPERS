import asyncio
import aiohttp
from PIL import Image
from io import BytesIO

from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
import io
from PySide6.QtWidgets import QApplication, QLabel

from model.RecipeModel import RecipeModel


async def load_image(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            image_data = await response.read()
    image = Image.open(io.BytesIO(image_data))
    return image

async def main():

    recipes = RecipeModel().getAllRecipes()
    app = QApplication([])
    n = 0
    try:
        for i in recipes:
            if n > 10:
                break
            # Load the image asynchronously
            image = await load_image(i.image)

            # Display the image using PySide6
            label = QLabel()
            pixmap = QPixmap()
            pixmap.convertFromImage(ImageQt(image))
            label.setPixmap(pixmap)
            label.show()
            n += 1
    except Exception as e:
        pass

    app.exec()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

#
#
