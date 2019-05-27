import setuptools


setuptools.setup(
    name = 'vtk_tools',
    version = '0.0.2a0',
    packages = setuptools.find_packages(),
    install_requires = [
        'vtk',
        'numpy',
        'scipy',
        'matplotlib']
)
