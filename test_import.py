import numpy
import theano
assert theano.config.device == "cpu" # the convnet will compiled/run for CPU, (THEANO_FLAGS="device=cpu" python test_import)
assert theano.config.floatX == "float32"

import lasagne
from lasagne.layers import Conv3DLayer
import nibabel

import sys
if sys.argv[1] == "with_convaffine":
	import model_apply_6tissues_mini
