from glob import glob
from setuptools import setup

package_name = 'soma_kit_hub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dominic Price',
    maintainer_email='dominic.price@nottingham.ac.uk',
    description='Soma Kit hub implementation',
    license='AGPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hub = soma_kit_hub.hub:main',
            'test_publisher = soma_kit_hub.test_publisher:main',
            'test_subscriber = soma_kit_hub.test_subscriber:main'
        ],
    },
)
