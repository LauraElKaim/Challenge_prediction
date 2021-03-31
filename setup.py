from setuptools import setup
from bikeprediction import __version__ as current_version

setup(
  name='bikeprediction_elk',
  version=current_version,
  description='Prediction and visualization of bike traffic in Montpellier',
  url='https://github.com/LauraElKaim/Challenge_prediction.git',
  author='ElKaimLaura',
  author_email='laura.el-kaim@etu.umontpellier.fr',
  license='MIT',
  packages=['bikeprediction','bikeprediction.data', 'bikeprediction.io',  'bikeprediction.preprocess', 'bikeprediction.vis'],
  zip_safe=False
)