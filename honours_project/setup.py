from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'honours_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share/' + package_name, 'sdf'), glob('sdf/*')),
        (os.path.join('share/' + package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share/' + package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share/' + package_name, 'models', 'honours_project_world'), glob('models/honours_project_world/**/*', recursive=True)),
    ],
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='u744434',
    maintainer_email='u744434@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
