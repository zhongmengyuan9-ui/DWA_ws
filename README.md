一、操控指令
1.仿真模型启动
#启动rviz2和gazebo仿真环境
ros2 launch mower_description mower_gazebo.launch.py 2>&1 | grep -v "blade_trajectory_controller"



# 启动一档
ros2 service call /mower/cutting_motor/control mower_description/srv/CuttingMotorControl "{speed_level: 1}"

# 启动二档
ros2 service call /mower/cutting_motor/control mower_description/srv/CuttingMotorControl "{speed_level: 2}"

# 启动三档
ros2 service call /mower/cutting_motor/control mower_description/srv/CuttingMotorControl "{speed_level: 3}"

# 关闭电机
ros2 service call /mower/cutting_motor/control mower_description/srv/CuttingMotorControl "{speed_level: 0}"


二、DWA局部避障验证
1.编译
colcon build --symlink-install
source install/setup.bash

# 2. 启动 Gazebo + 机器人模型 + 独立 DWA 局部规划节点
ros2 launch mower_dwa_local_planner dwa_demo.launch.py 2>&1 | grep -v "blade_trajectory_controller"

# 3. 在 RViz 中使用 “2D Goal Pose” 往 /goal_pose 发目标点
#    RViz 固定坐标系已配置为 odom，DWA 节点会直接读取该目标

# 4. 如果不想手动点目标，也可以直接给静态目标做验证
ros2 launch mower_dwa_local_planner dwa_demo.launch.py gui:=false rviz:=false use_static_goal:=true goal_x:=4.0 goal_y:=0.0

# 5. 观察关键话题
ros2 topic echo /cmd_vel
ros2 topic echo /dwa/best_path
ros2 topic echo /odom
ros2 topic echo /scan
