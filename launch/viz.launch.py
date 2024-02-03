import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    composable_node = ComposableNode(node_name='viz', namespace='apriltag', package='apriltag_viz', node_plugin='AprilVizNode', extra_arguments=[{'use_intra_process_comms': True}],)
    container = ComposableNodeContainer(
            node_name='tag_container',
            node_namespace='apriltag',
            package='rclcpp_components',
            node_executable='component_container',
            composable_node_descriptions=[composable_node],
            remappings=[("/apriltag/image", "/camera/image")],
            output='screen'
    )

    return launch.LaunchDescription([container])
