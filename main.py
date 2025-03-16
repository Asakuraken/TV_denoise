import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle, denoise_tv_bregman
from utils import read_image

def tv_denoise(image, weight=0.1, method='chambolle-dual'):
    if method == 'chambolle-dual':
        denoised_image = denoise_tv_chambolle(image, weight=weight, channel_axis=-1)
    elif method == 'bregman':
        denoised_image = denoise_tv_bregman(image, weight=weight, channel_axis=-1)
    else:
        raise ValueError(f"Invalid method {method}.")
    return denoised_image


if __name__ == "__main__":
    image_path = "image1.jpeg" 
    method = 'chambolle-dual'
    is_gray = True
    image = read_image(image_path, is_gray)

    noisy_image = image + 0.1 * np.random.normal(size=image.shape)
    noisy_image = np.clip(noisy_image, 0, 1)

    denoised_image = tv_denoise(noisy_image, weight=0.2)


    print(noisy_image.dtype)

    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title("Original Image")
    ax[0].axis("off")

    ax[1].imshow(noisy_image, cmap='gray')
    ax[1].set_title("Noisy Image")
    ax[1].axis("off")

    ax[2].imshow(denoised_image, cmap='gray')
    ax[2].set_title("Denoised Image (TV)")
    ax[2].axis("off")

    plt.show()