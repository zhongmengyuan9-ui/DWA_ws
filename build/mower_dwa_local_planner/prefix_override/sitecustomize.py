import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/q/Algorithm_research/DWA_ws/install/mower_dwa_local_planner'
