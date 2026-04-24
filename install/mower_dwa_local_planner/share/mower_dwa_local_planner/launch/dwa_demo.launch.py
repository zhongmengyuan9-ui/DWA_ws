import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    mower_description_share = get_package_share_directory('mower_description')
    dwa_share = get_package_share_directory('mower_dwa_local_planner')

    default_world = os.path.join(mower_description_share, 'worlds', 'room_world_open.world')
    default_params = os.path.join(dwa_share, 'config', 'dwa_params.yaml')
    mower_gazebo_launch = os.path.join(mower_description_share, 'launch', 'mower_gazebo.launch.py')

    world = LaunchConfiguration('world')
    gui = LaunchConfiguration('gui')
    rviz = LaunchConfiguration('rviz')
    use_sim_time = LaunchConfiguration('use_sim_time')
    dwa_params_file = LaunchConfiguration('dwa_params_file')
    use_static_goal = LaunchConfiguration('use_static_goal')
    goal_x = LaunchConfiguration('goal_x')
    goal_y = LaunchConfiguration('goal_y')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(mower_gazebo_launch),
        launch_arguments={
            'world': world,
            'gui': gui,
            'rviz': rviz,
            'use_sim_time': use_sim_time,
        }.items(),
    )

    planner = Node(
        package='mower_dwa_local_planner',
        executable='dwa_local_planner',
        name='dwa_local_planner',
        output='screen',
        parameters=[
            dwa_params_file,
            {
                'use_sim_time': ParameterValue(use_sim_time, value_type=bool),
                'use_static_goal': ParameterValue(use_static_goal, value_type=bool),
                'static_goal_x': ParameterValue(goal_x, value_type=float),
                'static_goal_y': ParameterValue(goal_y, value_type=float),
            },
        ],
    )

    return LaunchDescription([
        DeclareLaunchArgument('world', default_value=default_world, description='Gazebo world'),
        DeclareLaunchArgument('gui', default_value='true', description='Start Gazebo GUI'),
        DeclareLaunchArgument('rviz', default_value='true', description='Start RViz'),
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation clock'),
        DeclareLaunchArgument('dwa_params_file', default_value=default_params, description='DWA parameter file'),
        DeclareLaunchArgument('use_static_goal', default_value='false', description='Drive to a fixed goal without RViz'),
        DeclareLaunchArgument('goal_x', default_value='4.0', description='Static goal x in odom'),
        DeclareLaunchArgument('goal_y', default_value='0.0', description='Static goal y in odom'),
        gazebo,
        planner,
    ])
