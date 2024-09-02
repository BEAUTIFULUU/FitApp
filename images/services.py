from django.core.files.uploadedfile import InMemoryUploadedFile
from images.validators import validate_image
from images.models import ProductImage
from food.models import Product


def create_product_image(image: InMemoryUploadedFile, product: Product) -> None:
    validate_image(uploaded_image=image)
    ProductImage.objects.create(image=image, product=product)
