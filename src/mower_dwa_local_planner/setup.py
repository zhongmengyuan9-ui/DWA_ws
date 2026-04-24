from setuptools import setup

package_name = 'mower_dwa_local_planner'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/dwa_demo.launch.py']),
        ('share/' + package_name + '/config', ['config/dwa_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='q',
    maintainer_email='q@todo.todo',
    description='Standalone DWA local obstacle avoidance for the mower Gazebo model.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dwa_local_planner = mower_dwa_local_planner.dwa_local_planner:main',
        ],
    },
)
