# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup

package_name = 'fps_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yamato Okada',
    maintainer_email='s24c1031tu@s.chibakoudai.jp',
    description='FPS monitor package',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_sim = fps_monitor.sensor_sim:main',
            'fps_calc = fps_monitor.fps_calc:main',
        ],
    },
)
