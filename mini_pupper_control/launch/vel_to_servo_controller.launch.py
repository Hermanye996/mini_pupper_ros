#!/usr/bin/env python3
#
# Copyright 2023 MangDang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This program is based on ros official humble tutorials,
# https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes.html


from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

from launch_ros.actions import Node


def generate_launch_description():
    namespace = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_namespace_cmd = DeclareLaunchArgument(
        name='namespace', default_value='mini_pupper',
    )

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        name='use_sim_time', default_value='false',
    )

    return LaunchDescription([
        declare_namespace_cmd,
        declare_use_sim_time_cmd,

        Node(
            package='mini_pupper_control',
            executable='vel_to_servo_controller',
            name='vel_to_servo_controller',
            parameters=[{'namespace': namespace,
                         'use_sim_time': use_sim_time}],
            output='screen'
        ),
    ])
