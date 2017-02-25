import os
import sys
from distutils.core import setup
from glob import glob


class NodeModulesMissing(Exception):
    "raised when node_modules directory is not found"
    pass


if 'develop' in sys.argv or any(a.startswith('bdist') for a in sys.argv):
    import setuptools

# Ensure that js has been built. This does not guaruntee that the packages
# are update to date. In the future we might do a more expensive check
# involving file hashes, but only on sdist and bdist builds.
if not os.path.exists('node_modules'):
    raise NodeModulesMissing("Before Python package can be installed or built, "
                             "JavaScript components must be built using npm. "
                             "Run the following and then retry: "
                             "\nnpm install")

setup_args = dict(
    name                 = 'jupyterhub_labextension',
    scripts              = glob(os.path.join('cli_scripts', '*')),
    version              = '0.1.0',
    packages             = ['jupyterhub_labextension'],
    author               = 'Project Jupyter',
    author_email         = 'jupyter@googlegroups.com',
    keywords             = ['jupyterlab', 'jupyterlab extension'],
    include_package_data = True,
    install_requires = [
        'jupyterlab>=0.16.2',
        'jupyterhub>=0.7.0',
    ]
)

if __name__ == '__main__':
    setup(**setup_args)
