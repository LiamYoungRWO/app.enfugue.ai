# type: ignore
# adapted from https://github.com/ProjectNUWA/DragNUWA
__all__ = [
    "GeneralLPIPSWithDiscriminator",
    "LatentLPIPS",
]

from enfugue.diffusion.animate.dragnuwa.svd.modules.autoencoding.losses.discriminator_loss import GeneralLPIPSWithDiscriminator
from enfugue.diffusion.animate.dragnuwa.svd.modules.autoencoding.lpips import LatentLPIPS