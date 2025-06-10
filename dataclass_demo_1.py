from dataclasses import dataclass


@dataclass
class Point3d:
    """
    定义三维空间的一个点
    """
    x: int
    y: int
    z: int


if __name__ == '__main__':
    p1 = Point3d(100, 200, 300)
    p2 = Point3d(100, 200, 300)
    p3 = Point3d(100, 200, 600)
    print(p1)  # 输出: Point3d(x=100, y=200, z=300)
    print(p2)  # 输出: Point3d(x=100, y=200, z=300)
    print(p3)  # 输出: Point3d(x=100, y=200, z=600)
    print(p1 == p2)  # 输出: True
    print(p1 == p3)  # 输出: False
