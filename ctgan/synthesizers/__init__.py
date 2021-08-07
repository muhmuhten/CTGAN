"""Synthesizers module."""
from ctgan.synthesizers.ctgan import CTGAN
from ctgan.synthesizers.tvae import TVAE
from ctgan.synthesizers.dp_ctgan import DPCTGAN
from ctgan.synthesizers.adp_ctgan import ADPCTGAN

__all__ = (
    'CTGAN',
    'TVAE',
    'DPCTGAN',
    'ADPCTGAN'
)


def get_all_synthesizers():
    return {name: globals()[name] for name in __all__}
