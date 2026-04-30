import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_mower_description = get_package_share_directory('mower_description')

    default_world_path = os.path.join(pkg_mower_description, 'worlds', 'room_world_open.world')
    default_rviz_config = os.path.join(pkg_mower_description, 'config', 'rviz', 'mower_gazebo.rviz')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world = LaunchConfiguration('world', default=default_world_path)

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={
            'world': world,
            'extra_gazebo_args': '-s libgazebo_ros_api_plugin.so',
        }.items()
    )

    gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        ),
        condition=IfCondition(LaunchConfiguration('gui', default='true'))
    )

    urdf_path = os.path.join(pkg_mower_description, 'urdf', 'mower.urdf')
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': use_sim_time}],
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'gmower', '-topic', 'robot_description', '-x', '0', '-y', '0', '-z', '0.1', '-b'],
        output='screen'
    )

    delete_stale_entity = ExecuteProcess(
        cmd=[
            'ros2', 'service', 'call',
            '/delete_entity',
            'gazebo_msgs/srv/DeleteEntity',
            '{name: gmower}'
        ],
        output='screen'
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('mower_rvizconfig')],
        parameters=[{'use_sim_time': use_sim_time}],
        condition=IfCondition(LaunchConfiguration('mower_rviz'))
    )

    cutting_motor_controller = Node(
        package='mower_description',
        executable='cutting_motor_controller.py',
        name='cutting_motor_controller',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )

    gear_marker_publisher = Node(
        package='mower_description',
        executable='gear_marker_publisher.py',
        name='gear_marker_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )


    # 注意：
    # 旧的 indicator_light_controller.py 不再启动。
    # 指示灯颜色改由 Gazebo 插件直接订阅 /mower/cutting_motor/status 来控制。

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true',
                              description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument('headless', default_value='false',
                              description='Whether to run gzclient'),
        DeclareLaunchArgument('gui', default_value='true',
                              description='Whether to run gzclient'),
        DeclareLaunchArgument('world', default_value=default_world_path,
                              description='Gazebo world file'),
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Whether to run RViz2'),
        DeclareLaunchArgument('rvizconfig', default_value=default_rviz_config,
                              description='Path to RViz2 config file'),
        DeclareLaunchArgument('mower_rviz', default_value=LaunchConfiguration('rviz'),
                              description='(Internal) Whether to run RViz2 for mower_description'),
        DeclareLaunchArgument('mower_rvizconfig', default_value=LaunchConfiguration('rvizconfig'),
                              description='(Internal) RViz2 config path for mower_description'),

        gazebo,
        gazebo_client,
        robot_state_publisher,
        TimerAction(period=2.0, actions=[delete_stale_entity]),
        TimerAction(period=4.0, actions=[spawn_entity]),
        cutting_motor_controller,
        gear_marker_publisher,
        rviz2,
    ])
