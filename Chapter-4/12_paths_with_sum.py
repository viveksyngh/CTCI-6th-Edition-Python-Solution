"""
You are given a binary tree in which each node contains an integrer value(which might be positive or negative).
Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at 
the root or leaf, but it must go downwands (travelling only from parent nodes to child nodes). 
"""


# Solution 1
def get_path_with_sum(root, target_sum):
    if root is None:
        return 0
    
    # Get all paths starting from this node
    paths_from_root = get_path_with_sum_from_this_node(root.left, target_sum, 0)

    # Get paths starting from left and right child
    path_from_left = get_path_with_sum(root.left, target_sum)
    path_from_right = get_path_with_sum(root.right, target_sum)

    return paths_from_root + path_from_left + path_from_right



def get_path_with_sum_from_this_node(root, target_sum, current_sum):
    if root is None:
        return 0
    
    total_paths = 0
    current_sum += root.data
    if current_sum == target_sum:
        total_paths += 1
    
    total_paths += get_path_with_sum_from_this_node(root.left, target_sum, current_sum)
    total_paths += get_path_with_sum_from_this_node(root.right, target_sum, current_sum)
    return total_paths

# Solution 2

def count_paths_with_sum(root, target_sum):
    return count_paths_with_sum_helper(root, target_sum, 0, {})

def count_paths_with_sum_helper(root, target_sum, running_sum, running_map_sum):
    if root is None:
        return 0
    
    running_sum += root.data
    required_sum = running_sum - target_sum

    total_paths = running_map_sum.get(required_sum, 0)

    if running_sum == target_sum:
        total_paths += 1
    
    running_map_sum[running_sum] = running_map_sum.get(required_sum, 0) + 1
    # Recurse and find path sums in left and right
    total_paths += count_paths_with_sum_helper(root.left, target_sum, running_sum, running_map_sum)
    total_paths += count_paths_with_sum_helper(root.right, target_sum, running_sum, running_map_sum)

    running_map_sum[running_sum] = running_map_sum.get(required_sum, 0) - 1
    return total_paths

    

