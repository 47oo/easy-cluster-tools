#!/usr/bin/env python3
from ClusterShell.NodeSet import NodeSet
import argparse
import sys

def expand_patterns(node_pattern, ip_pattern):
    """使用ClusterShell的NodeSet和IPSet解析范围模式并进行顺序匹配"""
    nodes = list(NodeSet(node_pattern))
    ips = list(NodeSet(ip_pattern))
    
    if len(nodes) != len(ips):
        print(f"错误：节点数量({len(nodes)})与IP数量({len(ips)})不匹配")
        sys.exit(1)
        
    # 按顺序一对一绑定
    for node, ip in zip(nodes, ips):
        print(f"{node} {ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expand node and IP patterns and bind them sequentially.")
    parser.add_argument("node_pattern", help="Node pattern, e.g., node[0-1]")
    parser.add_argument("ip_pattern", help="IP pattern, e.g., 192.168.1.[1-2]")
    args = parser.parse_args()

    node_pattern = args.node_pattern
    ip_pattern = args.ip_pattern

    expand_patterns(node_pattern, ip_pattern)
