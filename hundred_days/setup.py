from setuptools import find_packages, setup

package_name = 'hundred_days'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siddarth',
    maintainer_email='siddarth.dayasagar@gmail.com',
    description='100daysofROS2: A developer initaitive to learn ROS2 ',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'day1 = hundred_days.day1_pub:main',
            'day1_sub = hundred_days.day1_sub:main'
        ],
    },
)
